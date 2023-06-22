# flake8: noqa
from itertools import product
import pytest
import unittest
from smolcalc import evaluate, evaluate_all


class TestSmolcalc(unittest.TestCase):

    def test_add(self):
        operator = "+"
        self.assertEqual(evaluate(f"{operator}5"), "5")
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
        self.assertEqual(evaluate(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++"), "Invalid syntax")

    def test_sub(self):
        operator = "-"
        self.assertEqual(evaluate(f"{operator}5"), "-5")
        self.assertEqual(evaluate(f"10{operator}5"), "5")
        self.assertEqual(evaluate(f"10{operator}5.1"), "4.9")
        self.assertEqual(evaluate(f"10{operator}(-5)"), "15")
        self.assertEqual(evaluate(f"10{operator}(+50)"), "-40")
        self.assertEqual(evaluate(f"10{operator}(-50)"), "60")
        self.assertEqual(evaluate(f"10{operator}(-50.1)"), "60.1")
        self.assertEqual(evaluate(f"0.0{operator}0"), "0")
        self.assertEqual(evaluate(f"{operator}5"), "-5")

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
        self.assertEqual(evaluate(f"0.0{operator}123123"), "0")
        self.assertEqual(evaluate(f"2{operator}2{operator}2{operator}2"), "65536")

        self.assertEqual(evaluate(f"{operator}."), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(.)"), "Invalid syntax")
        self.assertEqual(evaluate(f"{operator}(-(.))"), "Invalid syntax")

        # should return an error message
        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")
        self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

    def test_fac(self):
        operator = "!"
        self.assertEqual(evaluate(f"(-12){operator}"), "runtime math error (no negative numbers)")
        self.assertEqual(evaluate(f"0{operator}"), "1")
        self.assertEqual(evaluate(f"10{operator}"), "3628800")
        self.assertEqual(evaluate(f"(10-20){operator}"), "runtime math error (no negative numbers)")
        self.assertEqual(evaluate(f"(25.6){operator}"), "runtime math error (only whole numbers)")
        self.assertEqual(evaluate(f"(-25){operator}"), "runtime math error (no negative numbers)")
        self.assertEqual(evaluate(f"(){operator}"), "Invalid syntax")

        self.assertEqual(evaluate(f"((3){operator}){operator}"), "720")

        self.assertEqual(evaluate(f"{operator}"), "Invalid syntax")

        # gamma func
        self.assertEqual(evaluate(f"10.1{operator}", special=True), "454760.7514415857")
        self.assertEqual(evaluate(f"-10.1{operator}", special=True), "-454760.7514415857")

    def test_ln(self):
        operator = "ln"  # ln()

        # create version of ln e.g lN Ln LN ln
        upperchar = list(operator.upper())
        lowerchar = list(operator.lower())
        chars = list(zip(upperchar, lowerchar))
        operators = ["".join(x) for x in product(*chars)]

        for operator in operators:
            self.assertEqual(evaluate(f"{operator}(-12)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(0)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(10)"), "2.302585092994046")
            self.assertEqual(evaluate(f"{operator}(10-20)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(25.6)"), "3.242592351485517")
            self.assertEqual(evaluate(f"{operator}(-25)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}()"), "Invalid syntax")
            self.assertEqual(evaluate(f"{operator}(5"), "Invalid syntax")

            self.assertEqual(evaluate(f"ln(ln(3))"), "0.0940478276166991")

            self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")

        self.assertEqual(evaluate(f"l"), "Invalid syntax")
        self.assertEqual(evaluate(f"l4"), "Illegal character at position (Ln:1, Col:2, Pos:2) '4'")

    def test_lg(self):
        operator = "lg"  # lg()

        upperchar = list(operator.upper())
        lowerchar = list(operator.lower())
        chars = list(zip(upperchar, lowerchar))
        operators = ["".join(x) for x in product(*chars)]

        for operator in operators:
            self.assertEqual(evaluate(f"{operator}(-12)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(0)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(10)"), "1")
            self.assertEqual(evaluate(f"{operator}(10-20)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(25.6)"), "1.4082399653118496")
            self.assertEqual(evaluate(f"{operator}(-25)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}()"), "Invalid syntax")
            self.assertEqual(evaluate(f"{operator}(5"), "Invalid syntax")

            self.assertEqual(evaluate(f"{operator}(lg(3))"), "-0.3213712361305426")

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

        self.assertEqual(evaluate(f"p"), "Invalid syntax")
        self.assertEqual(evaluate(f"p4"), "Illegal character at position (Ln:1, Col:2, Pos:2) '4'")

    def test_e(self):
        operator = "e"

        upperchar = list(operator.upper())
        lowerchar = list(operator.lower())
        chars = list(zip(upperchar, lowerchar))
        operators = ["".join(x) for x in product(*chars)]

        for operator in operators:
            self.assertEqual(evaluate(f"{operator}"), "2.718281828459045")
            self.assertEqual(evaluate(f"-{operator}"), "-2.718281828459045")
            self.assertEqual(evaluate(f"{operator}^2"), "7.3890560989306495")
            self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")
            self.assertEqual(evaluate(f"-{operator}*{operator}"), "-7.3890560989306495")
            self.assertEqual(evaluate(f"ln({operator})"), "1")

    def test_sqrt(self):
        operator = "sqrt"  # sqrt()

        upperchar = list(operator.upper())
        lowerchar = list(operator.lower())
        chars = list(zip(upperchar, lowerchar))
        operators = ["".join(x) for x in product(*chars)]

        for operator in operators:
            self.assertEqual(evaluate(f"{operator}(-12)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(0)"), "0")
            self.assertEqual(evaluate(f"{operator}(10)"), "3.1622776601683795")
            self.assertEqual(evaluate(f"{operator}(10-20)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(25.6)"), "5.059644256269407")
            self.assertEqual(evaluate(f"{operator}(-25)"), "math domain error (complex numbers not supported)")
            self.assertEqual(evaluate(f"{operator}(100)"), "10")

            self.assertEqual(evaluate(f"{operator}(sqrt(3))"), "1.3160740129524924")

            self.assertEqual(evaluate(f"10.1{operator}"), "Invalid syntax")
            self.assertEqual(evaluate(f"{operator}(5"), "Invalid syntax")

    def test_syntx(self):
        self.assertEqual("0", evaluate(f"( ( ( ( ( (.) ) ) ) ) ) "))
        self.assertEqual(evaluate(f"+1-1+1-1+1-1+1-1"), "0")
        self.assertEqual(evaluate(f"(((2+3)*(6-5))^((-pi)*23-(43*0.5)+6)*7)"), "3.20512717698112e-61")
        self.assertEqual(evaluate(f"())()"), "Invalid syntax")
        self.assertEqual(evaluate(f"1+2+3"), "6")
        self.assertEqual(evaluate(f""), "an empty expression cannot be evaluated")
        self.assertEqual(evaluate(f" ( ( ( (.) ) ) ) ) "), "Invalid syntax")
        self.assertEqual(evaluate(f"()"), "Invalid syntax")
        self.assertEqual(evaluate(f"("), "Invalid syntax")
        self.assertEqual(evaluate(f"(4"), "Invalid syntax")
        self.assertEqual(evaluate(f")("), "Invalid syntax")
        self.assertEqual(evaluate(f"eqwrrzuitttfh"), "Illegal character at position (Ln:1, Col:2, Pos:2) 'q'")
        self.assertEqual(evaluate(f"8/2*(2+2)"), "16")
        self.assertEqual(evaluate(f"(8/2^2*(2+2)^6*8)"), "65536")
        self.assertEqual(evaluate(f"pi^pi^pi^pi"), "math range error")
        self.assertEqual(evaluate(f"6/2*(1+2)"), "9")
        self.assertEqual(evaluate(f"100_000"), "100000")
        self.assertEqual(evaluate(f"_1__00_0_00"), "100000")
        self.assertEqual(evaluate(f"__10_0_00_0_+56_7"), "100567")
        self.assertEqual(evaluate(f"______________________________1________________00"), "100")
        self.assertEqual(evaluate(f"254235_-235"), "254000")
        self.assertEqual(evaluate(f"254235_-235"), "254000")
        self.assertEqual(evaluate(f"(12-12)!", decimal_separator=".", special=False), "1")
        self.assertEqual(evaluate(f"()!()!())!()!()!!)!))", decimal_separator=".", special=True), "Invalid syntax")
        self.assertEqual(evaluate(f"(.)!(.)!())!(.)!()!!)!))", decimal_separator=".", special=True), "Invalid syntax")
        self.assertEqual(evaluate(f"1!!!!", decimal_separator=",", special=False), "Invalid syntax")
        self.assertEqual(evaluate(f",1!1!", decimal_separator=",", special=True), "Invalid syntax")

    def test_decimal_separator(self):
        self.assertEqual(evaluate("1.0"), "1")
        self.assertEqual(evaluate("1,0"), "Illegal character at position (Ln:1, Col:2, Pos:2) ','")
        self.assertEqual(evaluate("1,0", decimal_separator=","), "1")
        self.assertEqual(evaluate("1,0", decimal_separator="asdfa"), "'asdfa' is not a valid decimal_separator")

        self.assertEqual(evaluate("1,0", decimal_separator=34.4),
                         "decimal_separator is type: str, but type was given:<class 'float'>")
        self.assertEqual(evaluate("1,0", decimal_separator=34),
                         "decimal_separator is type: str, but type was given:<class 'int'>")
        self.assertEqual(evaluate("1,0", decimal_separator=[3, 4]),
                         "decimal_separator is type: str, but type was given:<class 'list'>")
        self.assertEqual(evaluate("1,0", decimal_separator=print),
                         "decimal_separator is type: str, but type was given:<class 'builtin_function_or_method'>")

    def test_tab_size(self):
        self.assertEqual(evaluate("1,0", tab_size=print),
                         "tab_size is type: int, but type was given:<class 'builtin_function_or_method'>")

        self.assertEqual(evaluate("1.0", tab_size=233),"1")
        self.assertEqual(evaluate("\t1,0", tab_size=3), "Illegal character at position (Ln:1, Col:5, Pos:3) ','")

    def test_special_separator(self):
        self.assertEqual(evaluate("1.0", special=34.4),
                         "special is type: bool, but type was given:<class 'float'>")
        self.assertEqual(evaluate("1.0", special=34),
                         "special is type: bool, but type was given:<class 'int'>")
        self.assertEqual(evaluate("1.0", special="uzr"),
                         "special is type: bool, but type was given:<class 'str'>")
        self.assertEqual(evaluate("1.0", special=[0]),
                         "special is type: bool, but type was given:<class 'list'>")
        self.assertEqual(evaluate("1.0", special=bool),
                         "special is type: bool, but type was given:<class 'type'>")

    def test_eval(self):
        self.assertEqual(evaluate(None), "expression is type: str, but type was given:<class 'NoneType'>")
        self.assertEqual(evaluate(2345345), "expression is type: str, but type was given:<class 'int'>")
        self.assertEqual(evaluate(2345.545), "expression is type: str, but type was given:<class 'float'>")
        self.assertEqual(evaluate(("dfsa", 12)), "expression is type: str, but type was given:<class 'tuple'>")
        self.assertEqual(evaluate([34, "wer"]), "expression is type: str, but type was given:<class 'list'>")
        self.assertEqual(evaluate({34, 3453, 3453, 4, 3}), "expression is type: str, but type was given:<class 'set'>")
        self.assertEqual(evaluate({"rtt": "lol"}), "expression is type: str, but type was given:<class 'dict'>")
        self.assertEqual(evaluate("1234+,5", decimal_separator=","), "1234,5")

    def test_eval_all(self):
        self.assertEqual(evaluate_all(["4+4"]), ["8"])
        self.assertEqual(evaluate_all(["4+4"], special=True), ["8"])

        # errors

        with self.assertRaises(Exception) as context:
            evaluate_all(["4+4"], decimal_separator=7887)
        self.assertTrue("decimal_separator is type: str, list or NoneType, but type was given:<class 'int'>" in str(
            context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all(["4+4"], special=[])
        self.assertTrue("length special list != expressions list" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all(None)
        self.assertTrue("expressions is type: '<class 'NoneType'>' and not type: list" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all(None)
        self.assertTrue("expressions is type: '<class 'NoneType'>' and not type: list" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all([34534, 3245, 345.56, [], {}, ""])
        self.assertTrue(
            "expression in expressions is type: str, but type was given:<class 'list'>" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all(["1", "1", "1", "1", "1"], special=68)
        self.assertTrue(
            "special is type: str, list or NoneType, but type was given:<class 'int'>" in str(context.exception))

        with self.assertRaises(Exception) as context:
            evaluate_all(["1", "1", "1", "1", "1"], [",", ".", ",", "."])
        self.assertTrue("length decimal_separator list != expressions list" in str(context.exception))

        self.assertEqual(evaluate_all(["1", "1", "1", "1", "1"], [",", ".", ",", ".", ","]), ["1", "1", "1", "1", "1"])

        self.assertEqual(
            evaluate_all([",1", ".1", ",1", ".1", ",1"], [",", ".", ",", ".", ","], [True, True, True, True, False]),
            ["0,1", "0.1", "0,1", "0.1", "0,1"])

        self.assertEqual(evaluate_all([",1", ",1", ",1", ",1", ",1"], ","),
                         ["0,1", "0,1", "0,1", "0,1", "0,1"])

        self.assertEqual(evaluate_all([".1", ".1", ".1", ".1", ".1"], "."),
                         ["0.1", "0.1", "0.1", "0.1", "0.1"])


if __name__ == '__main__':
    unittest.main()
