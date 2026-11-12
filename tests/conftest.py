"""Shared fixtures: load gh-issues-import.py as a module and replace the network layer."""
import glob, importlib.util, json, os, re, sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")
sys.path.insert(0, ROOT)


def load_json(*parts):
    with open(os.path.join(FIXTURES, *parts), encoding="utf-8") as f:
        return json.load(f)


def all_issues():
    return [load_json("issues", os.path.basename(p)) for p in sorted(glob.glob(os.path.join(FIXTURES, "issues", "*.json")))]


def comments_for(number):
    path = os.path.join(FIXTURES, "comments", "issue_%03d_comments.json" % number)
    return load_json("comments", os.path.basename(path)) if os.path.exists(path) else []


@pytest.fixture(scope="session")
def ghi():
    spec = importlib.util.spec_from_file_location("ghi", os.path.join(ROOT, "gh-issues-import.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FakeGitHub:
    """Serves recorded fixtures for GET requests and records POST bodies."""

    def __init__(self):
        self.posts = []
        self.gets = []
        self.next_number = 1000

    def __call__(self, which, url, post_data=None):
        if post_data is not None:
            self.posts.append((which, url, post_data))
            self.next_number += 1
            return dict(post_data, number=self.next_number, id=self.next_number)
        self.gets.append((which, url))
        path, _, qs = url.partition("?")
        params = dict(p.split("=", 1) for p in qs.split("&") if "=" in p)
        page = int(params.get("page", 1))
        per_page = int(params.get("per_page", 30))
        m = re.fullmatch(r"issues/(\d+)/comments", path)
        if m:
            data = comments_for(int(m.group(1)))
            return data[(page - 1) * per_page: page * per_page]
        m = re.fullmatch(r"issues/(\d+)", path)
        if m:
            return load_json("issues", "issue_%03d.json" % int(m.group(1)))
        if path == "issues":
            data = all_issues()
            state = params.get("state", "open")
            if state != "all":
                data = [i for i in data if i["state"] == state]
            return data[(page - 1) * per_page: page * per_page]
        if path == "labels":
            return load_json("labels", "labels.json")
        if path.startswith("milestones"):
            return load_json("milestones", "milestones.json")
        raise AssertionError("unexpected request: " + url)


@pytest.fixture
def github(ghi, monkeypatch):
    fake = FakeGitHub()
    monkeypatch.setattr(ghi, "send_request", fake)
    return fake
