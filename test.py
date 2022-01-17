import unittest
from lib import *

class TestLib(unittest.TestCase):
    def test_add(self):
        # prepare 
        n1, n2 = 5, 10

        # result 
        result = add(n1, n2)

        # testing
        self.assertEqual(result, 15)
        self.assertIsInstance(result, int)

    def test_sub(self):
        # prepare 
        n1, n2 = 5, 10

        # result 
        result = sub(n1, n2)

        # testing
        self.assertEqual(result, 5)
        self.assertIsInstance(result, int)

    def test_mul(self):
        # prepare 
        n1, n2 = 5, 10

        # result 
        result = mul(n1, n2)

        # testing
        self.assertEqual(result, 50)
        self.assertIsInstance(result, int)

    def test_div(self):
        # prepare 
        n1, n2 = 5, 10

        # result 
        result = div(n1, n2)

        # testing
        self.assertEqual(result, 0)
        self.assertIsInstance(result, int)



if __name__ == "__main__":
    unittest.main()
