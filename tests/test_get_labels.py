def test_get_labels_uses_expected_endpoint(ghi, github):
    result = ghi.get_labels("source")
    assert github.gets == [("source", "labels")]
    names = [l["name"] for l in result]
    assert "bug" in names and len(names) == 12
