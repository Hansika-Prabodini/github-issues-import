import pytest

from tests.conftest import comments_for, load_json



def test_issue_001_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 1)
    assert issue["number"] == 1
    assert issue["title"] == 'Page config config milestone format label template format'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/1")]


def test_issue_001_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_001.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(1)]


def test_issue_001_labels(ghi):
    issue = load_json("issues", "issue_001.json")
    assert sorted(l["name"] for l in issue["labels"]) == []


def test_issue_002_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 2)
    assert issue["number"] == 2
    assert issue["title"] == 'Closed request enterprise'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/2")]


def test_issue_002_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_002.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(2)]


def test_issue_002_labels(ghi):
    issue = load_json("issues", "issue_002.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['duplicate', 'enhancement', 'help wanted']


def test_issue_003_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 3)
    assert issue["number"] == 3
    assert issue["title"] == 'Error page comment token open'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/3")]


def test_issue_003_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_003.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(3)]


def test_issue_003_labels(ghi):
    issue = load_json("issues", "issue_003.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['bug']


def test_issue_004_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 4)
    assert issue["number"] == 4
    assert issue["title"] == 'Comment api issue label milestone source'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/4")]


def test_issue_004_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_004.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(4)]


def test_issue_004_labels(ghi):
    issue = load_json("issues", "issue_004.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['help wanted']


def test_issue_005_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 5)
    assert issue["number"] == 5
    assert issue["title"] == 'Enterprise github request config issue'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/5")]


def test_issue_005_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_005.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(5)]


def test_issue_005_labels(ghi):
    issue = load_json("issues", "issue_005.json")
    assert sorted(l["name"] for l in issue["labels"]) == []


def test_issue_006_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 6)
    assert issue["number"] == 6
    assert issue["title"] == 'Import open closed config open'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/6")]


def test_issue_006_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_006.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(6)]


def test_issue_006_labels(ghi):
    issue = load_json("issues", "issue_006.json")
    assert sorted(l["name"] for l in issue["labels"]) == []
