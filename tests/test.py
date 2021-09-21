import unittest
from smolcalc.calculator import calculator

class Testsmolcalc(unittest.TestCase):

    def test_add(self):
        operator = "+"
        self.assertEqual(calculator(f"10{operator}5"), "15")
        self.assertEqual(calculator(f"10{operator}5.1"), "15.1")
        self.assertEqual(calculator(f"10{operator}(-5)"), "5")
        self.assertEqual(calculator(f"10{operator}(+50)"), "60")
        self.assertEqual(calculator(f"10{operator}(-50)"), "-40")
        self.assertEqual(calculator(f"10{operator}(-50.1)"), "-40.1")
        self.assertEqual(calculator(f"0.0{operator}0"),"0")

        # just weird
        self.assertEqual(calculator(f"{operator}."), "0")
        self.assertEqual(calculator(f"{operator}(.)"), "0")
        self.assertEqual(calculator(f"{operator}(-(.))"), "0")

        # should return an error message
        self.assertEqual(calculator(f"{operator}"), "'NoneType' object has no attribute 'type'")
        self.assertEqual(calculator(f"10.1{operator}"), "'NoneType' object has no attribute 'type'")



    def test_sub(self):
        operator = "-"
        self.assertEqual(calculator(f"10{operator}5"), "5")
        self.assertEqual(calculator(f"10{operator}5.1"), "4.9")
        self.assertEqual(calculator(f"10{operator}(-5)"), "15")
        self.assertEqual(calculator(f"10{operator}(+50)"), "-40")
        self.assertEqual(calculator(f"10{operator}(-50)"), "60")
        self.assertEqual(calculator(f"10{operator}(-50.1)"), "60.1")
        self.assertEqual(calculator(f"0.0{operator}0"), "0")

        # just weird
        self.assertEqual(calculator(f"{operator}."), "0")
        self.assertEqual(calculator(f"{operator}(.)"), "0")
        self.assertEqual(calculator(f"{operator}(-(.))"), "0")

        # should return an error message
        self.assertEqual(calculator(f"{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")


    def test_mult(self):
        operator = "*"
        self.assertEqual(calculator(f"10{operator}5"), "50")
        self.assertEqual(calculator(f"10{operator}5.1"), "51")
        self.assertEqual(calculator(f"10{operator}(-5)"), "-50")
        self.assertEqual(calculator(f"10{operator}(+50)"), "500")
        self.assertEqual(calculator(f"10{operator}(-50)"), "-500")
        self.assertEqual(calculator(f"10{operator}(-50.1)"), "-501")
        self.assertEqual(calculator(f"0.0{operator}0"), "0")

        # just weird
        self.assertEqual(calculator(f"{operator}."), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(calculator(f"{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")


if __name__ == '__main__':
    unittest.main()