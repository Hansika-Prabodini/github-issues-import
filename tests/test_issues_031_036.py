import pytest

from tests.conftest import comments_for, load_json



def test_issue_031_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 31)
    assert issue["number"] == 31
    assert issue["title"] == 'Request format date source body'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/31")]


def test_issue_031_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_031.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(31)]


def test_issue_031_labels(ghi):
    issue = load_json("issues", "issue_031.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['duplicate']


def test_issue_032_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 32)
    assert issue["number"] == 32
    assert issue["title"] == 'Github closed target source comment label api config'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/32")]


def test_issue_032_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_032.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(32)]


def test_issue_032_labels(ghi):
    issue = load_json("issues", "issue_032.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['Example Issue', 'bug', 'help wanted']


def test_issue_033_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 33)
    assert issue["number"] == 33
    assert issue["title"] == 'Closed repository response closed'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/33")]


def test_issue_033_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_033.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(33)]


def test_issue_033_labels(ghi):
    issue = load_json("issues", "issue_033.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['help wanted']


def test_issue_034_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 34)
    assert issue["number"] == 34
    assert issue["title"] == 'Retry retry title'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/34")]


def test_issue_034_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_034.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(34)]


def test_issue_034_labels(ghi):
    issue = load_json("issues", "issue_034.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['documentation', 'duplicate', 'security']


def test_issue_035_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 35)
    assert issue["number"] == 35
    assert issue["title"] == 'Closed request repository api'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/35")]


def test_issue_035_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_035.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 35
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(35)]


def test_issue_035_labels(ghi):
    issue = load_json("issues", "issue_035.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['In progress', 'bug']


def test_issue_036_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 36)
    assert issue["number"] == 36
    assert issue["title"] == 'Response page enterprise comment open retry label state'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/36")]


def test_issue_036_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_036.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(36)]


def test_issue_036_labels(ghi):
    issue = load_json("issues", "issue_036.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['duplicate', 'invalid']
