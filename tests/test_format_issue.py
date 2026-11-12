import pytest

from tests.conftest import load_json


@pytest.mark.parametrize("n", [1, 11, 22])
def test_format_issue_renders_template(ghi, n):
    issue = load_json("issues", "issue_%03d.json" % n)
    out = ghi.format_issue({
        "user_name": issue["user"]["login"], "user_url": issue["user"]["html_url"],
        "user_avatar": issue["user"]["avatar_url"], "date": ghi.format_date(issue["created_at"]),
        "url": issue["html_url"], "body": issue["body"],
    })
    assert issue["user"]["login"] in out
    assert issue["body"] in out
