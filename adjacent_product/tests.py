import unittest
from largest_adjacent_product import largest_product
def parse_string(s):
    return [int(c) for c in list(s)]

class TestLargestProduct(unittest.TestCase):
    def test_small_input(self):
        s = '1234'
        digits = [int(c) for c in list(s)]
        product = largest_product(digits, 2)
        self.assertEqual(product, 12)
        print "tested small input"

    def test_largest_in_between(self):
        s = '123789123'
        digits = [int(c) for c in list(s)]
        product = largest_product(digits, 3)
        self.assertEqual(product, 504)
        print "tested largest in between"
    
    def test_one_zero(self):
        s = '23023'
        digits = [int(c) for c in list(s)]
        product = largest_product(digits, 2)
        self.assertEqual(product, 6)
        print "tested single zero"
    
    def test_zero_in_between(self):
        s = '123012301234'
        digits = [int(c) for c in list(s)]
        product = largest_product(digits, 4)
        self.assertEqual(product, 24)

if __name__ == '__main__':
    unittest.main()
