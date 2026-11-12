import pytest

from tests.conftest import comments_for, load_json



def test_issue_025_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 25)
    assert issue["number"] == 25
    assert issue["title"] == 'Open date label'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/25")]


def test_issue_025_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_025.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(25)]


def test_issue_025_labels(ghi):
    issue = load_json("issues", "issue_025.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['good first issue', 'invalid', 'question']


def test_issue_026_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 26)
    assert issue["number"] == 26
    assert issue["title"] == 'Comment retry title source page format body token'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/26")]


def test_issue_026_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_026.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(26)]


def test_issue_026_labels(ghi):
    issue = load_json("issues", "issue_026.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['In progress', 'bug']


def test_issue_027_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 27)
    assert issue["number"] == 27
    assert issue["title"] == 'Request open target'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/27")]


def test_issue_027_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_027.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(27)]


def test_issue_027_labels(ghi):
    issue = load_json("issues", "issue_027.json")
    assert sorted(l["name"] for l in issue["labels"]) == []


def test_issue_028_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 28)
    assert issue["number"] == 28
    assert issue["title"] == 'Page source retry'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/28")]


def test_issue_028_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_028.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 35
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(28)]


def test_issue_028_labels(ghi):
    issue = load_json("issues", "issue_028.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['documentation', 'security']


def test_issue_029_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 29)
    assert issue["number"] == 29
    assert issue["title"] == 'Response import token open'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/29")]


def test_issue_029_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_029.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(29)]


def test_issue_029_labels(ghi):
    issue = load_json("issues", "issue_029.json")
    assert sorted(l["name"] for l in issue["labels"]) == []


def test_issue_030_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 30)
    assert issue["number"] == 30
    assert issue["title"] == 'Comment retry closed'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/30")]


def test_issue_030_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_030.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 3
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(30)]


def test_issue_030_labels(ghi):
    issue = load_json("issues", "issue_030.json")
    assert sorted(l["name"] for l in issue["labels"]) == []
