import unittest

from report import remove_none_values, sort_pages


class Tests(unittest.TestCase):
    def test_remove_none_values(self):
        self.assertEqual({}, remove_none_values({"1": None}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1", "2": None}))
        self.assertEqual({}, remove_none_values({}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1"}))

    def test_sort_pages(self):
        self.assertEqual(
            sort_pages({"first": 45, "third": 15, "second": 25}),
            [("first", 45), ("second", 25), ("third", 15)],
        )
        self.assertEqual(
            sort_pages({"first": 45, "third": 46, "second": 47}),
            [("second", 47), ("third", 46), ("first", 45)],
        )


if __name__ == "__main__":
    unittest.main()