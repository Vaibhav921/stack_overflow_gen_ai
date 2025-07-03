import unittest
from controller import fetch_stackoverflow_answers


class TestFetchStackOverflowAnswers(unittest.TestCase):
    def test_fetch_stackoverflow_answers_success(self):

        results = fetch_stackoverflow_answers("reverse a list in python")

        self.assertIsInstance(results, list)
        self.assertTrue(any(r["answers"] > 0 for r in results))
        self.assertTrue(any("reverse" in r["title"].lower() for r in results))

    def test_fetch_stackoverflow_answers_empty(self):
        results = fetch_stackoverflow_answers("asdkfjhasdkjfhaskjdfhaskjdfh")
        self.assertEqual(results, [])

    def test_fetch_stackoverflow_answers_http_error(self):
        import controller

        original_url = (
            controller.STACKOVERFLOW_API_URL
            if hasattr(controller, "STACKOVERFLOW_API_URL")
            else None
        )
        try:
            controller.STACKOVERFLOW_API_URL = (
                "https://api.stackexchange.com/invalid_endpoint"
            )
            with self.assertRaises(Exception):
                fetch_stackoverflow_answers("error test")
        finally:
            if original_url:
                controller.STACKOVERFLOW_API_URL = original_url


if __name__ == "__main__":
    unittest.main()
