def test_get_milestones_uses_expected_endpoint(ghi, github):
    result = ghi.get_milestones("source")
    assert github.gets == [("source", "milestones?state=open")]
    assert [m["number"] for m in result] == [1, 2, 3, 4]
