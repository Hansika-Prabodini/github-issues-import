import pytest

from tests.conftest import comments_for, load_json



def test_issue_037_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 37)
    assert issue["number"] == 37
    assert issue["title"] == 'Source enterprise date import response'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/37")]


def test_issue_037_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_037.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(37)]


def test_issue_037_labels(ghi):
    issue = load_json("issues", "issue_037.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['bug', 'help wanted', 'invalid']


def test_issue_038_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 38)
    assert issue["number"] == 38
    assert issue["title"] == 'Config comment token milestone api'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/38")]


def test_issue_038_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_038.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 3
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(38)]


def test_issue_038_labels(ghi):
    issue = load_json("issues", "issue_038.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['Example Issue', 'wontfix']


def test_issue_039_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 39)
    assert issue["number"] == 39
    assert issue["title"] == 'Label github github milestone label import'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/39")]


def test_issue_039_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_039.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(39)]


def test_issue_039_labels(ghi):
    issue = load_json("issues", "issue_039.json")
    assert sorted(l["name"] for l in issue["labels"]) == []


def test_issue_040_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 40)
    assert issue["number"] == 40
    assert issue["title"] == 'Body unicode closed body issue'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/40")]


def test_issue_040_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_040.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(40)]


def test_issue_040_labels(ghi):
    issue = load_json("issues", "issue_040.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['good first issue']


def test_issue_041_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 41)
    assert issue["number"] == 41
    assert issue["title"] == 'Issue github body state retry'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/41")]


def test_issue_041_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_041.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(41)]


def test_issue_041_labels(ghi):
    issue = load_json("issues", "issue_041.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['bug']


def test_issue_042_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 42)
    assert issue["number"] == 42
    assert issue["title"] == 'Milestone api label state retry comment retry date'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/42")]


def test_issue_042_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_042.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 35
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(42)]


def test_issue_042_labels(ghi):
    issue = load_json("issues", "issue_042.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['documentation']
