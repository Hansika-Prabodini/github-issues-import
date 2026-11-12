import pytest

from tests.conftest import comments_for, load_json



def test_issue_007_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 7)
    assert issue["number"] == 7
    assert issue["title"] == 'Error format response'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/7")]


def test_issue_007_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_007.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 35
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(7)]


def test_issue_007_labels(ghi):
    issue = load_json("issues", "issue_007.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['bug', 'enhancement', 'wontfix']


def test_issue_008_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 8)
    assert issue["number"] == 8
    assert issue["title"] == 'Unicode issue token enterprise unicode error'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/8")]


def test_issue_008_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_008.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(8)]


def test_issue_008_labels(ghi):
    issue = load_json("issues", "issue_008.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['Example Issue', 'duplicate', 'help wanted']


def test_issue_009_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 9)
    assert issue["number"] == 9
    assert issue["title"] == 'Issue page error response'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/9")]


def test_issue_009_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_009.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 3
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(9)]


def test_issue_009_labels(ghi):
    issue = load_json("issues", "issue_009.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['wontfix']


def test_issue_010_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 10)
    assert issue["number"] == 10
    assert issue["title"] == 'Source response import unicode enterprise body label'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/10")]


def test_issue_010_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_010.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(10)]


def test_issue_010_labels(ghi):
    issue = load_json("issues", "issue_010.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['Example Issue', 'enhancement', 'good first issue']


def test_issue_011_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 11)
    assert issue["number"] == 11
    assert issue["title"] == 'Format closed api'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/11")]


def test_issue_011_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_011.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(11)]


def test_issue_011_labels(ghi):
    issue = load_json("issues", "issue_011.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['Example Issue']


def test_issue_012_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 12)
    assert issue["number"] == 12
    assert issue["title"] == 'Request import date closed'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/12")]


def test_issue_012_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_012.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(12)]


def test_issue_012_labels(ghi):
    issue = load_json("issues", "issue_012.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['Example Issue', 'invalid']
