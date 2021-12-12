from typing import Optional, Union

from smolcalc.lexer import Lexer
from smolcalc.parser_ import Parser
from smolcalc.interpreter import Interpreter


def evaluate(expression: str, decimal_separator: Optional[str] = None, special: Optional[bool] = None) -> str:
    """ function for calculating a math expression in form of a string

    :param special: bool if True factorial uses the gamma function
    :param expression: math expression in form of a string
    :param decimal_separator: decimal separator . or,
    :return: (results or exception) in form of a string
    """

    try:
        if not isinstance(expression, str):
            raise TypeError(f"expression is type: str, but type was given:{type(expression)}")

        if not (isinstance(decimal_separator, str) or decimal_separator is None):
            raise TypeError(f"decimal_separator is type: str, but type was given:{type(decimal_separator)}")

        if not (isinstance(special, bool) or special is None):
            raise TypeError(f"special is type: bool, but type was given:{type(special)}")

        if decimal_separator is None or decimal_separator == ".":
            decimal_separator = "."
        elif decimal_separator == ",":
            decimal_separator = ","
        else:
            raise ValueError(f"'{decimal_separator}' is not a valid decimal_separator")

        if special is None:
            special = False

        lexer = Lexer(expression, decimal_separator)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()

        if tree:
            interpreter = Interpreter(special)
            value = interpreter.visit(tree)
            str_value: str = str(value)

            if decimal_separator == "," and "." in str_value:
                str_value = str_value.replace(".", decimal_separator)

            return str_value
        else:
            raise Exception("an empty expression cannot be evaluated")
    except Exception as e:  # change
        return str(e)


def evaluate_all(expressions: list[str], decimal_separator: Optional[Union[list[str], str]] = None,
                 special: Optional[Union[list[bool], bool]] = None) -> list[str]:
    """ function for calculating multiple math expressions given in form of list of strings (calls function evaluate)

    :param expressions: list of strings
    :param decimal_separator: . or , or a list of decimal_separator for every expression
    :param special: True or False or a list of bool for every expression
    :return: list of strings
    """

    if not isinstance(expressions, list):
        raise TypeError(f"expressions is type: '{type(expressions)}' and not type: list")

    if not all([True if isinstance(i, str) else False for i in expressions]):
        raise TypeError(f"expression in expressions is type: str, but type was given:{type(expressions)}")

    if decimal_separator is None or isinstance(decimal_separator, list) or isinstance(decimal_separator, str):

        if isinstance(decimal_separator, str):
            decimal_separators: Union[list[str], list[None]] = [decimal_separator] * len(expressions)
        elif decimal_separator is None:
            decimal_separators = [None] * len(expressions)

        if isinstance(decimal_separator, list):
            if len(decimal_separator) != len(expressions):
                raise Exception("length decimal_separator list != expressions list")
            decimal_separators = decimal_separator

    else:
        raise TypeError(
            f"decimal_separator is type: str, list or NoneType, but type was given:{type(decimal_separator)}")

    if special is None or isinstance(special, list) or isinstance(special, bool):

        if isinstance(special, bool):
            special_list: Union[list[bool], list[None]] = [special] * len(expressions)
        elif special is None:
            special_list = [None] * len(expressions)

        if isinstance(special, list):
            if len(special) != len(expressions):
                raise Exception("length special list != expressions list")
            special_list = special

    else:
        raise TypeError(f"special is type: str, list or NoneType, but type was given:{type(special)}")

    return [evaluate(expression=e, decimal_separator=decimal_separators[i], special=special_list[i]) for i, e in
            enumerate(expressions)]
