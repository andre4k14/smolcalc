from smolcalc.lexer import Lexer
from smolcalc.parser_ import Parser
from smolcalc.interpreter import Interpreter

def evaluate(text) -> str:
    """ Method for calculating a math expression in form of a string

    :param text: math expression in form of a string
    :return: (results or exception) in form of a string
    """
    try:
        if not isinstance(text,str):
            return "function received an argument of wrong type (not string)"
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if tree:
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            value = str(value)
            return value
        else:
            return "an empty expression cannot be evaluated"
    except Exception as e: # change
        return str(e)

def evaluate_all(expressions) -> list:
    return [evaluate(i) for i in expressions ]
