import sys
import signal
from smolcalc import evaluate
from smolcalc.lexer import Lexer
from smolcalc.parser_ import Parser
from smolcalc.interpreter import Interpreter

sys.setrecursionlimit(5000)  # find a way to not need to increase the recursion limit


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def run_and_print(exp: str) -> None:
    try:
        print(f"Input: {exp}")
        lexer = Lexer(exp, ".", 1)
        tokens = list(lexer.generate_tokens())
        print(f"Tokens: {tokens}")
        parser = Parser(tokens)
        tree = parser.parse()
        print(f"Tree: {tree}")

        if tree:
            interpreter = Interpreter(False)
            value = interpreter.evaluate(tree)
            print(f"Result: {value}\n")
    except Exception as e:  # change
        print(e)


def main():
    run_and_print("34.0*3(we r _34t")
    run_and_print(")!")
    run_and_print("5!")
    run_and_print("5!!")
    run_and_print("-8^2")
    run_and_print("(-2)^2!")
    run_and_print("(-2)^2")
    run_and_print("((-2)^2)!")
    run_and_print("5!")

    """
      print(evaluate(
          "(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("
          "(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("
          "(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("
          "(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("
          "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((69.420))))))))))))))))))))))))))))))))))))))))))))"
          "))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
          "))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
          "))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
          "))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
          "))))))))))) )))))"))
      """

    print(evaluate("(1234"))
    print(evaluate("10.0!"))
    print(evaluate("(-10.0)!"))
    print(evaluate([0, 0]))
    print(evaluate(None))
    print(evaluate("(((2+3)*(6-5))^((-pi)*23-(43*0.5)+6)*7)"))
    print(evaluate("ln(-12)"))
    print(evaluate(" 10^(50)"))
    print(evaluate("10+5.1"))
    print(evaluate("0^0"))
    print(evaluate("2*(2.7 -1 )"))
    print(evaluate("1+2*6/67"))
    print(evaluate("lg(10)"))
    print(evaluate("10.1sqrt"))
    print(evaluate("-7,1!+7!", special=True, decimal_separator=","))
    print(evaluate("0,1!", special=True, decimal_separator=","))
    print(evaluate("12++4"))
    print(evaluate("12--4"))
    print(evaluate("12+---++-+--++--++-+-++---++-+--++--+-+--+-++-+++--+--4"))
    print(evaluate("0,1!", special=True, decimal_separator=","))
    print(evaluate("1\tc2++4"))
    print(evaluate("0/0"))
    print(evaluate("10.1ln"))
    help(evaluate)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
