import unittest
from calc import Calculator

class CalcTestCase(unittest.TestCase):
    def setUp(self):
        self.C = Calculator()
    def test_multiplication_with_ints(self):
        self.assertEqual( self.C.multiply( 5 , 5), 25 )
    def test_add_with_ints(self):
        self.assertEqual( self.C.add( 1, 5), 6)
        self.assertEqual( self.C.add( 2, 2), 4)
    def test_div(self):
        self.assertEqual(self.C.div(10,2), 5)


if __name__ == "__main__":
    unittest.main()


