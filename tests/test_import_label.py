import pytest

from tests.conftest import load_json

LABELS = load_json("labels", "labels.json")


@pytest.mark.parametrize("label", LABELS, ids=[l["name"] for l in LABELS])
def test_import_label_posts_only_name_and_color(ghi, github, label):
    source = dict(label, url="https://api.github.com/x", id=99)
    ghi.import_label(source)
    (which, url, body), = github.posts
    assert (which, url) == ("target", "labels")
    assert body == {"name": label["name"], "color": label["color"]}
