import pytest


@pytest.mark.parametrize("ids", [[3, 1, 2], [48, 7], [10], [5, 4, 3, 2, 1]])
def test_issues_by_id_are_sorted(ghi, github, ids):
    got = [i["number"] for i in ghi.get_issues_by_id("source", ids)]
    assert got == sorted(ids)


def test_issues_by_id_accepts_string_ids(ghi, github):
    got = [i["number"] for i in ghi.get_issues_by_id("source", ["12", "2"])]
    assert got == [2, 12]
