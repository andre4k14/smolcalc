from smolcalc.lexer import Lexer
from smolcalc.parser_ import Parser
from smolcalc.interpreter import Interpreter


def evaluate(expression, decimal_separator=None, special=None) -> str:
    """ Method for calculating a math expression in form of a string

    :param expression: math expression in form of a string
    :param decimal_separator: decimal separator . or,
    :return: (results or exception) in form of a string
    """

    try:
        if decimal_separator is None or decimal_separator == ".":
            decimal_separator = "."
        elif decimal_separator == ",":
            decimal_separator = ","
        else:
            raise Exception(f"'{decimal_separator}' is not a valid decimal_separator")

        if special is None or not special:
            special = False
        elif special:
            special = True
        else:
            raise Exception(f"'{special}' is not a valid special")

        if not isinstance(expression, str):
            return "function received an argument of wrong type (not string)"
        lexer = Lexer(expression, decimal_separator)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if tree:
            interpreter = Interpreter(special)
            value = interpreter.visit(tree)
            value = str(value)

            if decimal_separator == "," and "." in value:
                value = value.replace(".", decimal_separator)

            return value
        else:
            return "an empty expression cannot be evaluated"
    except Exception as e:  # change
        return str(e)


def evaluate_all(expressions, decimal_separator=None, special_=None) -> list:
    """ Method for calculating multiple math expressions given in form of list of strings (calls method evaluate)

    :param expressions: list of strings
    :param decimal_separator: . or , or a list of decimal_separator for every expression
    :param special_: True or False or a list of decimal_separator for every expression
    :return: list of strings
    """

    if not isinstance(expressions, list):
        raise Exception(f"expressions is type: '{type(expressions)}' and not type: list")

    if not all([True if isinstance(i, str) else False for i in expressions]):
        raise Exception(f"expression in expressions is not type: str")

    if decimal_separator is None or isinstance(decimal_separator, list) or isinstance(decimal_separator, str):

        if isinstance(decimal_separator, str):
            decimal_separators = [decimal_separator for x in range(len(expressions))]
        elif decimal_separator is None:
            decimal_separators = [None for x in range(len(expressions))]

        if isinstance(decimal_separator, list):
            if len(decimal_separator) != len(expressions):
                raise Exception("length decimal_separator list != expressions list")
            decimal_separators = decimal_separator

    if special_ is None or isinstance(special_, list) or isinstance(special_, bool):

        if isinstance(special_, bool):
            special_list = [special_ for x in range(len(expressions))]
        elif special_ is None:
            special_list = [None for x in range(len(expressions))]

        if isinstance(special_, list):
            if len(special) != len(expressions):
                raise Exception("length special list != expressions list")
            special_list = special_

        return [evaluate(expression=e, decimal_separator=decimal_separators[i], special=special_list[i]) for i, e in
                enumerate(expressions)]


    else:
        raise Exception("expressions to evaluate not in datatype: list")
