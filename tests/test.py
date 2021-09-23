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
        self.assertEqual(calculator(f"0.0{operator}0"), "0")

        # just weird
        self.assertEqual(calculator(f"{operator}."), "0")
        self.assertEqual(calculator(f"{operator}(.)"), "0")
        self.assertEqual(calculator(f"{operator}(-(.))"), "0")

        # should return an error message
        self.assertEqual(calculator(f"{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

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

        self.assertEqual(calculator(f"{operator}."), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(calculator(f"{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

    def test_div(self):
        operator = "/"
        self.assertEqual(calculator(f"10{operator}5"), "2")
        self.assertEqual(calculator(f"10{operator}5.1"), "1.9607843137254903")
        self.assertEqual(calculator(f"10{operator}(-5)"), "-2")
        self.assertEqual(calculator(f"10{operator}(+50)"), "0.2")
        self.assertEqual(calculator(f"10{operator}(-50)"), "-0.2")
        self.assertEqual(calculator(f"10{operator}(-50.1)"), "-0.1996007984031936")
        self.assertEqual(calculator(f"0.0{operator}0"), "runtime math error (Division by zero)")

        self.assertEqual(calculator(f"{operator}."), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(calculator(f"{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

    def test_pow(self):
        operator = "^"
        self.assertEqual(calculator(f"10{operator}5"), "100000")
        self.assertEqual(calculator(f"10{operator}5.1"), "125892.54117941661")
        self.assertEqual(calculator(f"10{operator}(-5)"), "1e-05")
        self.assertEqual(calculator(f"10{operator}(+50)"), "1e+50")
        self.assertEqual(calculator(f"10{operator}(-50)"), "1e-50")
        self.assertEqual(calculator(f"10{operator}(-50.1)"), "7.943282347242789e-51")
        self.assertEqual(calculator(f"0.0{operator}0"), "0^0 is undefined.")

        self.assertEqual(calculator(f"{operator}."), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(calculator(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(calculator(f"{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

    def test_fac(self):
        operator = "!()"
        self.assertEqual(calculator(f"!(-12)"), "runtime math error (no negative numbers)")
        self.assertEqual(calculator(f"!(0)"), "1")
        self.assertEqual(calculator(f"!(10)"), "3628800")
        self.assertEqual(calculator(f"!(10-20)"), "runtime math error (no negative numbers)")
        self.assertEqual(calculator(f"!(25.6)"), "runtime math error (only whole numbers)")
        self.assertEqual(calculator(f"!(-25)"), "runtime math error (no negative numbers)")
        self.assertEqual(calculator(f"!()"), "Invalid syntax")

        self.assertEqual(calculator(f"!(!(3))"), "720")

        self.assertEqual(calculator(f"{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

    def test_ln(self):
        operator = "ln()"
        self.assertEqual(calculator(f"ln(-12)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"ln(0)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"ln(10)"), "2.302585092994046")
        self.assertEqual(calculator(f"ln(10-20)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"ln(25.6)"), "3.242592351485517")
        self.assertEqual(calculator(f"ln(-25)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"ln()"), "Invalid syntax")

        self.assertEqual(calculator(f"ln(ln(3))"), "0.0940478276166991")

        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

    def test_lg(self):
        operator = "lg()"
        self.assertEqual(calculator(f"lg(-12)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"lg(0)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"lg(10)"), "1")
        self.assertEqual(calculator(f"lg(10-20)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"lg(25.6)"), "1.4082399653118496")
        self.assertEqual(calculator(f"lg(-25)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"lg()"), "Invalid syntax")

        self.assertEqual(calculator(f"lg(lg(3))"), "-0.3213712361305426")

        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

    def test_pi(self):
        operator = "pi"
        self.assertEqual(calculator(f"{operator}"), "3.141592653589793")
        self.assertEqual(calculator(f"-{operator}"), "-3.141592653589793")
        self.assertEqual(calculator(f"{operator}^2"), "9.869604401089358")
        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")
        self.assertEqual(calculator(f"-{operator}*{operator}"), "-9.869604401089358")

    def test_sqrt(self):
        operator = "sqrt()"
        self.assertEqual(calculator(f"sqrt(-12)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"sqrt(0)"), "0")
        self.assertEqual(calculator(f"sqrt(10)"), "3.1622776601683795")
        self.assertEqual(calculator(f"sqrt(10-20)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"sqrt(25.6)"), "5.059644256269407")
        self.assertEqual(calculator(f"sqrt(-25)"), "math domain error (complex numbers not supported)")
        self.assertEqual(calculator(f"sqrt(100)"), "10")

        self.assertEqual(calculator(f"sqrt(sqrt(3))"), "1.3160740129524924")

        self.assertEqual(calculator(f"10.1{operator}"), "Invalid syntax")

    def test_syntx(self):
        self.assertEqual(calculator(f"( ( ( ( ( (.) ) ) ) ) ) "), "0")
        self.assertEqual(calculator(f"(((2+3)*(6-5))^((-pi)*23-(43*0.5)+6)*7)"), "3.20512717698112e-61")
        self.assertEqual(calculator(f"())()"), "Invalid syntax")
        self.assertEqual(calculator(f"1+2+3"), "6")
        self.assertEqual(calculator(f""), "an empty expression cannot be evaluated")
        self.assertEqual(calculator(f" ( ( ( (.) ) ) ) ) "), "Invalid syntax")
        self.assertEqual(calculator(f"()"), "Invalid syntax")
        self.assertEqual(calculator(f")("), "Invalid syntax")
        self.assertEqual(calculator(f"eqwrrzuitttfh"), "Illegal character 'e'")


if __name__ == '__main__':
    unittest.main()
