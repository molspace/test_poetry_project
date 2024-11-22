import unittest
from function import reverse

class TestFunctions(unittest.TestCase): 
    def test_reverse(self):
        # check list
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])
        # check tuple
        self.assertEqual(reverse((1, 2, 3)), (3, 2, 1))
        # check string
        self.assertEqual(reverse("abcdefg"), "gfedcba")
        # check set
        self.assertEqual(reverse({1, 2, 3}), [3, 2, 1])
        # check generator
        self.assertEqual(reverse(range(3)),  [2, 1, 0])
