from feed_animals import feedAnimals
import unittest

class TestFeedAnimals(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(feedAnimals([1, 2, 3, 4, 8], [8, 3, 9, 1, 7]), 5)

    def test_case_2(self):
        self.assertEqual(feedAnimals([1, 2, 3], [2, 1, 2]), 2)

    def test_case_3(self):
        self.assertEqual(feedAnimals([4, 5, 6], [1, 2, 3]), 0)

    def test_case_4(self):
        self.assertEqual(feedAnimals([], [2, 3, 4]), 0)

    def test_case_5(self):
        self.assertEqual(feedAnimals([1, 2, 3], []), 0)

    def test_case_6(self):
        self.assertEqual(feedAnimals([5, 5, 5], [5, 5, 5]), 3)

    def test_case_7(self):
        self.assertEqual(feedAnimals([10, 20, 30], [5, 15, 25, 35]), 3)

    def test_case_8(self):
        self.assertEqual(feedAnimals([1, 2, 3, 4, 5], [5, 5, 5, 5, 5]), 5)

    def test_case_9(self):
        self.assertEqual(feedAnimals([5], [3]), 0)

    def test_case_10(self):
        self.assertEqual(feedAnimals([5, 6], [5, 6]), 2)

if __name__ == '__main__':
    unittest.main()