import pytest

from tests.conftest import all_issues


@pytest.mark.parametrize("state", ["open", "closed", "all"])
def test_pages_until_exhausted(ghi, github, state):
    got = list(ghi.get_issues_by_state("source", state))
    want = [i for i in all_issues() if state == "all" or i["state"] == state]
    assert [i["number"] for i in got] == [i["number"] for i in want]
