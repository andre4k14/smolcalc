from calculator.lexer import Lexer
from calculator.parser_ import Parser
from calculator.interpreter import Interpreter

def calculator(text):
    """ Method for calculating a math expression in form of string

    :param text: math expression in form of string
    :return: results or exception
    """
    try:
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if tree:
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            return value
    except Exception as e:
        return e

