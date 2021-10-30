import unittest
from itertools import product

from smolcalc.calculator import evaluate, evaluate_all


class TestSmolcalc(unittest.TestCase):

    def test_add(self):
        operator = "+"
        self.assertEqual(evaluate(f"10{operator}5"), "15")
        self.assertEqual(evaluate(f"10{operator}5.1"), "15.1")
        self.assertEqual(evaluate(f"10{operator}(-5)"), "5")
        self.assertEqual(evaluate(f"10{operator}(+50)"), "60")
        self.assertEqual(evaluate(f"10{operator}(-50)"), "-40")
        self.assertEqual(evaluate(f"10{operator}(-50.1)"), "-40.1")
        self.assertEqual(evaluate(f"0.0{operator}0"), "0")

        # just weird
        self.assertEqual(evaluate(f"{operator}."), "0")
        self.assertEqual(evaluate(f"{operator}(.)"), "0")
        self.assertEqual(evaluate(f"{operator}(-(.))"), "0")

        # should return an error message
        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")
        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_sub(self):
        operator = "-"
        self.assertEqual(evaluate(f"10{operator}5"), "5")
        self.assertEqual(evaluate(f"10{operator}5.1"), "4.9")
        self.assertEqual(evaluate(f"10{operator}(-5)"), "15")
        self.assertEqual(evaluate(f"10{operator}(+50)"), "-40")
        self.assertEqual(evaluate(f"10{operator}(-50)"), "60")
        self.assertEqual(evaluate(f"10{operator}(-50.1)"), "60.1")
        self.assertEqual(evaluate(f"0.0{operator}0"), "0")

        # just weird
        self.assertEqual(evaluate(f"{operator}."), "0")
        self.assertEqual(evaluate(f"{operator}(.)"), "0")
        self.assertEqual(evaluate(f"{operator}(-(.))"), "0")

        # should return an error message
        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")
        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_mult(self):
        operator = "*"
        self.assertEqual(evaluate(f"10{operator}5"), "50")
        self.assertEqual(evaluate(f"10{operator}5.1"), "51")
        self.assertEqual(evaluate(f"10{operator}(-5)"), "-50")
        self.assertEqual(evaluate(f"10{operator}(+50)"), "500")
        self.assertEqual(evaluate(f"10{operator}(-50)"), "-500")
        self.assertEqual(evaluate(f"10{operator}(-50.1)"), "-501")
        self.assertEqual(evaluate(f"0.0{operator}0"), "0")

        self.assertEqual(evaluate(f"{operator}."), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")
        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_div(self):
        operator = "/"
        self.assertEqual(evaluate(f"10{operator}5"), "2")
        self.assertEqual(evaluate(f"10{operator}5.1"), "1.9607843137254903")
        self.assertEqual(evaluate(f"10{operator}(-5)"), "-2")
        self.assertEqual(evaluate(f"10{operator}(+50)"), "0.2")
        self.assertEqual(evaluate(f"10{operator}(-50)"), "-0.2")
        self.assertEqual(evaluate(f"10{operator}(-50.1)"), "-0.1996007984031936")
        self.assertEqual(evaluate(f"0.0{operator}0"), "runtime math error (Division by zero)")

        self.assertEqual(evaluate(f"{operator}."), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")
        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_pow(self):
        operator = "^"
        self.assertEqual(evaluate(f"10{operator}5"), "100000")
        self.assertEqual(evaluate(f"10{operator}5.1"), "125892.54117941661")
        self.assertEqual(evaluate(f"10{operator}(-5)"), "1e-05")
        self.assertEqual(evaluate(f"10{operator}(+50)"), "1e+50")
        self.assertEqual(evaluate(f"10{operator}(-50)"), "1e-50")
        self.assertEqual(evaluate(f"10{operator}(-50.1)"), "7.943282347242789e-51")
        self.assertEqual(evaluate(f"0.0{operator}0"), "0^0 is undefined.")
        self.assertEqual(evaluate(f"2{operator}2{operator}2{operator}2"), "65536")

        self.assertEqual(evaluate(f"{operator}."), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")
        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_fac(self):
        operator = "!()"
        self.assertEqual(evaluate(f"!(-12)"), "runtime math error (no negative numbers)")
        self.assertEqual(evaluate(f"!(0)"), "1")
        self.assertEqual(evaluate(f"!(10)"), "3628800")
        self.assertEqual(evaluate(f"!(10-20)"), "runtime math error (no negative numbers)")
        self.assertEqual(evaluate(f"!(25.6)"), "runtime math error (only whole numbers)")
        self.assertEqual(evaluate(f"!(-25)"), "runtime math error (no negative numbers)")
        self.assertEqual(evaluate(f"!()"), "Invalid syntax")

        self.assertEqual(evaluate(f"!(!(3))"), "720")

        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")
        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_ln(self):
        operator = "ln"  # ln()

        # create version of pi e.g PI Pi pI pi
        upperchar = list(operator.upper())
        lowerchar = list(operator.lower())
        chars = list(zip(upperchar, lowerchar))
        operators = ["".join(x) for x in product(*chars)]

        self.assertEqual(evaluate(f"{operator}(-12)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"{operator}(0)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"{operator}(10)"), "2.302585092994046")
        self.assertEqual(evaluate(f"{operator}(10-20)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"{operator}(25.6)"), "3.242592351485517")
        self.assertEqual(evaluate(f"{operator}(-25)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"{operator}()"), "Invalid syntax")

        self.assertEqual(evaluate(f"ln(ln(3))"), "0.0940478276166991")

        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_lg(self):
        operator = "lg()"
        self.assertEqual(evaluate(f"lg(-12)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"lg(0)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"lg(10)"), "1")
        self.assertEqual(evaluate(f"lg(10-20)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"lg(25.6)"), "1.4082399653118496")
        self.assertEqual(evaluate(f"lg(-25)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"lg()"), "Invalid syntax")

        self.assertEqual(evaluate(f"lg(lg(3))"), "-0.3213712361305426")

        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_pi(self):
        operator = "pi"

        # create version of pi e.g PI Pi pI pi
        upperchar = list(operator.upper())
        lowerchar = list(operator.lower())
        chars = list(zip(upperchar, lowerchar))
        operators = ["".join(x) for x in product(*chars)]

        for operator in operators:
            self.assertEqual(evaluate(f"{operator}"), "3.141592653589793")
            self.assertEqual(evaluate(f"-{operator}"), "-3.141592653589793")
            self.assertEqual(evaluate(f"{operator}^2"), "9.869604401089358")
            self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")
            self.assertEqual(evaluate(f"-{operator}*{operator}"), "-9.869604401089358")

    def test_sqrt(self):
        operator = "sqrt()"
        self.assertEqual(evaluate(f"sqrt(-12)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"sqrt(0)"), "0")
        self.assertEqual(evaluate(f"sqrt(10)"), "3.1622776601683795")
        self.assertEqual(evaluate(f"sqrt(10-20)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"sqrt(25.6)"), "5.059644256269407")
        self.assertEqual(evaluate(f"sqrt(-25)"), "math domain error (complex numbers not supported)")
        self.assertEqual(evaluate(f"sqrt(100)"), "10")

        self.assertEqual(evaluate(f"sqrt(sqrt(3))"), "1.3160740129524924")

        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_syntx(self):
        self.assertEqual(evaluate(f"( ( ( ( ( (.) ) ) ) ) ) "), "0")
        self.assertEqual(evaluate(f"(((2+3)*(6-5))^((-pi)*23-(43*0.5)+6)*7)"), "3.20512717698112e-61")
        self.assertEqual(evaluate(f"())()"), "Invalid syntax")
        self.assertEqual(evaluate(f"1+2+3"), "6")
        self.assertEqual(evaluate(f""), "an empty expression cannot be evaluated")
        self.assertEqual(evaluate(f" ( ( ( (.) ) ) ) ) "), "Invalid syntax")
        self.assertEqual(evaluate(f"()"), "Invalid syntax")
        self.assertEqual(evaluate(f")("), "Invalid syntax")
        self.assertEqual(evaluate(f"eqwrrzuitttfh"), "Illegal character 'e'")
        self.assertEqual(evaluate(f"8/2*(2+2)"), "16")
        self.assertEqual(evaluate(f"(8/2^2*(2+2)^6*8)"), "65536")
        self.assertEqual(evaluate(f"pi^pi^pi^pi"), "math range error")
        self.assertEqual(evaluate(f"6/2*(1+2)"), "9")
        self.assertEqual(evaluate(f"100_000"), "100000")
        self.assertEqual(evaluate(f"_1__00_0_00"), "100000")
        self.assertEqual(evaluate(f"__10_0_00_0_+56_7"), "100567")
        self.assertEqual(evaluate(f"______________________________1________________00"), "100")
        self.assertEqual(evaluate(f"254235_-235"), "254000")

    def test_decimal_separator(self):
        self.assertEqual(evaluate("1.0"), "1")
        self.assertEqual(evaluate("1,0"), "Illegal character ','")
        self.assertEqual(evaluate("1,0", decimal_separator=","), "1")
        self.assertEqual(evaluate("1,0", decimal_separator="asdfa"), "'asdfa' is not a valid decimal_separator")
        self.assertEqual(evaluate("1,0", decimal_separator=print),
                         "'<built-in function print>' is not a valid decimal_separator")
        self.assertEqual(evaluate("1,0", decimal_separator=34.4), "'34.4' is not a valid decimal_separator")
        self.assertEqual(evaluate("1,0", decimal_separator=34), "'34' is not a valid decimal_separator")
        self.assertEqual(evaluate("1,0", decimal_separator=[3, 4]), "'[3, 4]' is not a valid decimal_separator")

    def test_eval(self):
        self.assertEqual(evaluate(None), "function received an argument of wrong type (not string)")
        self.assertEqual(evaluate(2345345), "function received an argument of wrong type (not string)")
        self.assertEqual(evaluate(2345.545), "function received an argument of wrong type (not string)")
        self.assertEqual(evaluate(("dfsa", 12)), "function received an argument of wrong type (not string)")
        self.assertEqual(evaluate([34, "wer"]), "function received an argument of wrong type (not string)")
        self.assertEqual(evaluate({34, 3453, 3453, 4, 3}), "function received an argument of wrong type (not string)")
        self.assertEqual(evaluate({"rtt": "lol"}), "function received an argument of wrong type (not string)")
        self.assertEqual(evaluate("1234+,5", decimal_separator=","), "1234,5")

    def test_eval_all(self):
        with self.assertRaises(Exception) as context:
            evaluate_all(None)
        self.assertTrue("expressions is type: '<class 'NoneType'>' and not type: list" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all(None)
        self.assertTrue("expressions is type: '<class 'NoneType'>' and not type: list" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all([34534, 3245, 345.56, [], {}, ""])
        self.assertTrue("expression in expressions is not type: str" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all([34534, 3245, 345.56, [], {}, ""])
        self.assertTrue("expression in expressions is not type: str" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all(["1", "1", "1", "1", "1"], [",", ".", ",", "."])
        self.assertTrue("length decimal_separator list != expressions list" in str(context.exception))

        self.assertEqual(evaluate_all(["1", "1", "1", "1", "1"], [",", ".", ",", ".", ","]), ["1", "1", "1", "1", "1"])

        self.assertEqual(evaluate_all([",1", ".1", ",1", ".1", ",1"], [",", ".", ",", ".", ","]),
                         ["0,1", "0.1", "0,1", "0.1", "0,1"])

        self.assertEqual(evaluate_all([",1", ",1", ",1", ",1", ",1"],","),
                         ["0,1", "0,1", "0,1", "0,1", "0,1"])

        self.assertEqual(evaluate_all([".1", ".1", ".1", ".1", ".1"], "."),
                         ["0.1", "0.1", "0.1", "0.1", "0.1"])


if __name__ == '__main__':
    unittest.main()
