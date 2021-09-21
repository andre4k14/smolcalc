import unittest
from smolcalc.calculator import calculator

class Testsmolcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator("10+5"), "15")
        self.assertEqual(calculator("10+5.1"), "15.1")
        self.assertEqual(calculator("10+(-5)"), "5")
        self.assertEqual(calculator("10+(+50)"), "60")
        self.assertEqual(calculator("10+(-50)"), "-40")
        self.assertEqual(calculator("10+(-50.1)"), "-40.1")

        # just weird
        self.assertEqual(calculator("+."), "0")
        self.assertEqual(calculator("+(.)"), "0")
        self.assertEqual(calculator("+(-(.))"), "0")

        # should return an error message
        self.assertEqual(calculator("+"), "'NoneType' object has no attribute 'type'")
        self.assertEqual(calculator("10.1+"), "'NoneType' object has no attribute 'type'")



    def test_sub(self):
        self.assertEqual(calculator("10-5"), "5")
        self.assertEqual(calculator("10-5.1"), "4.9")
        self.assertEqual(calculator("10-(-5)"), "15")
        self.assertEqual(calculator("10-(+50)"), "-40")
        self.assertEqual(calculator("10-(-50)"), "60")
        self.assertEqual(calculator("10-(-50.1)"), "60.1")

        # just weird
        self.assertEqual(calculator("-."), "0")
        self.assertEqual(calculator("-(.)"), "0")
        self.assertEqual(calculator("-(+(.))"), "0")

        # should return an error message
        self.assertEqual(calculator("-"), "'NoneType' object has no attribute 'type'")
        self.assertEqual(calculator("10.1-"), "'NoneType' object has no attribute 'type'")

if __name__ == '__main__':
    unittest.main()