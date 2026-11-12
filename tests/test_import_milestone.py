import pytest

from tests.conftest import load_json

MILESTONES = load_json("milestones", "milestones.json")


@pytest.mark.parametrize("ms", MILESTONES, ids=[m["title"] for m in MILESTONES])
def test_import_milestone_posts_expected_fields(ghi, github, ms):
    ghi.import_milestone(dict(ms, number=77, url="https://api.github.com/x"))
    (which, url, body), = github.posts
    assert (which, url) == ("target", "milestones")
    assert set(body) == {"title", "state", "description", "due_on"}
