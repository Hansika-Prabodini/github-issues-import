import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).with_name("gh-issues-import.py")
spec = importlib.util.spec_from_file_location("gh_issues_import", MODULE_PATH)
gh_issues_import = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gh_issues_import)


class ImportMilestoneTests(unittest.TestCase):
    def test_import_milestone_sends_only_supported_fields(self):
        source = {
            "title": "Release 1.0",
            "state": "closed",
            "description": "Initial release",
            "due_on": "2025-01-01T00:00:00Z",
            "number": 42,
            "creator": {"login": "octocat"},
        }
        requests = []

        def send_request(which, url, post_data=None):
            requests.append((which, url, post_data))
            return {"title": source["title"]}

        original_send_request = gh_issues_import.send_request
        gh_issues_import.send_request = send_request
        try:
            gh_issues_import.import_milestone(source)
        finally:
            gh_issues_import.send_request = original_send_request

        self.assertEqual(
            requests,
            [
                (
                    "target",
                    "milestones",
                    {
                        "title": "Release 1.0",
                        "state": "open",
                        "description": "Initial release",
                        "due_on": "2025-01-01T00:00:00Z",
                    },
                )
            ],
        )


if __name__ == "__main__":
    unittest.main()
