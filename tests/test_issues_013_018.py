import pytest

from tests.conftest import comments_for, load_json



def test_issue_013_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 13)
    assert issue["number"] == 13
    assert issue["title"] == 'Closed api unicode'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/13")]


def test_issue_013_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_013.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(13)]


def test_issue_013_labels(ghi):
    issue = load_json("issues", "issue_013.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['enhancement', 'invalid']


def test_issue_014_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 14)
    assert issue["number"] == 14
    assert issue["title"] == 'Source enterprise body comment body retry'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/14")]


def test_issue_014_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_014.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 35
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(14)]


def test_issue_014_labels(ghi):
    issue = load_json("issues", "issue_014.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['documentation', 'question']


def test_issue_015_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 15)
    assert issue["number"] == 15
    assert issue["title"] == 'Import milestone import retry github github config open'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/15")]


def test_issue_015_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_015.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(15)]


def test_issue_015_labels(ghi):
    issue = load_json("issues", "issue_015.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['enhancement', 'question']


def test_issue_016_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 16)
    assert issue["number"] == 16
    assert issue["title"] == 'State target unicode label github date'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/16")]


def test_issue_016_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_016.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(16)]


def test_issue_016_labels(ghi):
    issue = load_json("issues", "issue_016.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['In progress', 'documentation', 'help wanted']


def test_issue_017_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 17)
    assert issue["number"] == 17
    assert issue["title"] == 'Closed api enterprise target target template'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/17")]


def test_issue_017_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_017.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(17)]


def test_issue_017_labels(ghi):
    issue = load_json("issues", "issue_017.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['documentation', 'invalid']


def test_issue_018_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 18)
    assert issue["number"] == 18
    assert issue["title"] == 'Comment page title template unicode body target title'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/18")]


def test_issue_018_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_018.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(18)]


def test_issue_018_labels(ghi):
    issue = load_json("issues", "issue_018.json")
    assert sorted(l["name"] for l in issue["labels"]) == []
