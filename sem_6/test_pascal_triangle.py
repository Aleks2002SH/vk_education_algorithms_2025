import unittest
from pascal_triangle import pascal_triangle
class TestPascalTriangle(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(pascal_triangle(0), [])

    def test_case_2(self):
        self.assertEqual(pascal_triangle(1), [[1]])

    def test_case_3(self):
        self.assertEqual(pascal_triangle(2), [[1], [1, 1]])

    def test_case_4(self):
        self.assertEqual(pascal_triangle(3), [[1], [1, 1], [1, 2, 1]])

    def test_case_5(self):
        self.assertEqual(pascal_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_case_6(self):
        self.assertEqual(pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_case_7(self):
        self.assertEqual(pascal_triangle(6), [
            [1], 
            [1, 1], 
            [1, 2, 1], 
            [1, 3, 3, 1], 
            [1, 4, 6, 4, 1], 
            [1, 5, 10, 10, 5, 1]
        ])

if __name__ == "__main__":
    unittest.main()