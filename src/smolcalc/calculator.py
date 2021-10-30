from smolcalc.lexer import Lexer
from smolcalc.parser_ import Parser
from smolcalc.interpreter import Interpreter


def evaluate(text, decimal_separator=None) -> str:
    """ Method for calculating a math expression in form of a string

    :param text: math expression in form of a string
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

        if not isinstance(text, str):
            return "function received an argument of wrong type (not string)"
        lexer = Lexer(text, decimal_separator)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if tree:
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            value = str(value)

            if decimal_separator == "," and "." in value:
                value = value.replace(".", decimal_separator)

            return value
        else:
            return "an empty expression cannot be evaluated"
    except Exception as e:  # change
        return str(e)


def evaluate_all(expressions, decimal_separator=None) -> list:
    """ Method for calculating multiple math expressions given in form of list of strings (calls method evaluate)

    :param expressions: list of strings
    :param decimal_separator: . or , or a list of decimal_separator for every expression
    :return: list of strings
    """

    if not isinstance(expressions, list):
        raise Exception(f"expressions is type: '{type(expressions)}' and not type: list")

    if not all([True if isinstance(i, str) else False for i in expressions]):
        raise Exception(f"expression in expressions is not type: str")

    if not decimal_separator is None or not isinstance(decimal_separator, list) or not isinstance(decimal_separator,
                                                                                                  str):
        raise Exception("expressions to evaluate not in datatype: list")

    if isinstance(decimal_separator, str):
        decimal_separators = [decimal_separator for x in range(len(expressions))]
    elif decimal_separator is None:
        decimal_separators = None

    if isinstance(decimal_separator, list):
        if len(decimal_separator) != len(expressions):
            raise Exception("length decimal_separator list != expressions list")
        decimal_separators = decimal_separator

    if not decimal_separators is None:
        return [evaluate(i, decimal_separator) for i in expressions]
    else:
        return [evaluate(i) for i in expressions]
