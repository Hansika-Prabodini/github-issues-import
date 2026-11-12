import pytest

from tests.conftest import comments_for, load_json



def test_issue_019_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 19)
    assert issue["number"] == 19
    assert issue["title"] == 'Comment state source label'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/19")]


def test_issue_019_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_019.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(19)]


def test_issue_019_labels(ghi):
    issue = load_json("issues", "issue_019.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['Example Issue', 'invalid']


def test_issue_020_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 20)
    assert issue["number"] == 20
    assert issue["title"] == 'Issue title github open source token response target'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/20")]


def test_issue_020_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_020.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(20)]


def test_issue_020_labels(ghi):
    issue = load_json("issues", "issue_020.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['documentation', 'help wanted', 'wontfix']


def test_issue_021_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 21)
    assert issue["number"] == 21
    assert issue["title"] == 'Error request page format template target milestone response'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/21")]


def test_issue_021_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_021.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 35
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(21)]


def test_issue_021_labels(ghi):
    issue = load_json("issues", "issue_021.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['enhancement', 'help wanted']


def test_issue_022_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 22)
    assert issue["number"] == 22
    assert issue["title"] == 'Milestone request repository repository response date config'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/22")]


def test_issue_022_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_022.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(22)]


def test_issue_022_labels(ghi):
    issue = load_json("issues", "issue_022.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['bug', 'enhancement', 'help wanted']


def test_issue_023_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 23)
    assert issue["number"] == 23
    assert issue["title"] == 'Unicode body title token response target'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/23")]


def test_issue_023_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_023.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(23)]


def test_issue_023_labels(ghi):
    issue = load_json("issues", "issue_023.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['bug', 'enhancement', 'question']


def test_issue_024_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 24)
    assert issue["number"] == 24
    assert issue["title"] == 'Unicode milestone page'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/24")]


def test_issue_024_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_024.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 3
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(24)]


def test_issue_024_labels(ghi):
    issue = load_json("issues", "issue_024.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['bug', 'help wanted']
