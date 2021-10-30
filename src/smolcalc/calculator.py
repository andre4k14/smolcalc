from smolcalc.lexer import Lexer
from smolcalc.parser_ import Parser
from smolcalc.interpreter import Interpreter

def evaluate(text,decimal_separator=None) -> str:
    """ Method for calculating a math expression in form of a string

    :param text: math expression in form of a string
    :param decimal_separator: decimal separator . or,
    :return: (results or exception) in form of a string
    """

    if (decimal_separator is None or decimal_separator == ".") and decimal_separator != ",":
        decimal_separator = "."
    else:
        decimal_separator = ","


    try:
        if not isinstance(text,str):
            return "function received an argument of wrong type (not string)"
        lexer = Lexer(text,decimal_separator)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if tree:
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            value = str(value)

            if decimal_separator == "," and "." in value:
                value = value.replace(".",decimal_separator)

            return value
        else:
            return "an empty expression cannot be evaluated"
    except Exception as e: # change
        return str(e)

def evaluate_all(expressions,decimal_separator=None) -> list:
    """ Method for calculating multiple math expressions given in form of list of strings (calls method evaluate)

    :param expressions: list of strings ()
    :return: list of strings
    """
    if isinstance(expressions,list):
        return [evaluate(i,decimal_separator) if isinstance(i,str) else "no string, not evaluated " for i in expressions ]
