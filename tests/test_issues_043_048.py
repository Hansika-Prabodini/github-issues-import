import pytest

from tests.conftest import comments_for, load_json



def test_issue_043_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 43)
    assert issue["number"] == 43
    assert issue["title"] == 'Github request date date source page unicode'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/43")]


def test_issue_043_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_043.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 0
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(43)]


def test_issue_043_labels(ghi):
    issue = load_json("issues", "issue_043.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['In progress']


def test_issue_044_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 44)
    assert issue["number"] == 44
    assert issue["title"] == 'Source request token milestone state api config issue'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/44")]


def test_issue_044_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_044.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(44)]


def test_issue_044_labels(ghi):
    issue = load_json("issues", "issue_044.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['In progress', 'good first issue']


def test_issue_045_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 45)
    assert issue["number"] == 45
    assert issue["title"] == 'Token state label template error state'
    assert issue["state"] == 'closed'
    assert github.gets == [("source", "issues/45")]


def test_issue_045_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_045.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 4
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(45)]


def test_issue_045_labels(ghi):
    issue = load_json("issues", "issue_045.json")
    assert sorted(l["name"] for l in issue["labels"]) == []


def test_issue_046_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 46)
    assert issue["number"] == 46
    assert issue["title"] == 'Token format import open'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/46")]


def test_issue_046_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_046.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 1
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(46)]


def test_issue_046_labels(ghi):
    issue = load_json("issues", "issue_046.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['security']


def test_issue_047_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 47)
    assert issue["number"] == 47
    assert issue["title"] == 'Page body date milestone token date template'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/47")]


def test_issue_047_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_047.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 3
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(47)]


def test_issue_047_labels(ghi):
    issue = load_json("issues", "issue_047.json")
    assert sorted(l["name"] for l in issue["labels"]) == []


def test_issue_048_fetch_by_id(ghi, github):
    issue = ghi.get_issue_by_id("source", 48)
    assert issue["number"] == 48
    assert issue["title"] == 'Page title issue label enterprise'
    assert issue["state"] == 'open'
    assert github.gets == [("source", "issues/48")]


def test_issue_048_all_comments_fetched(ghi, github):
    issue = load_json("issues", "issue_048.json")
    comments = list(ghi.get_comments_on_issue("source", issue) or [])
    assert len(comments) == 2
    assert [c["id"] for c in comments] == [c["id"] for c in comments_for(48)]


def test_issue_048_labels(ghi):
    issue = load_json("issues", "issue_048.json")
    assert sorted(l["name"] for l in issue["labels"]) == ['wontfix']
