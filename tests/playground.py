import sys
import signal
from smolcalc import evaluate
from smolcalc.lexer import Lexer

sys.setrecursionlimit(5000)


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def main():
    print(list(Lexer("ln(5", decimal_separator=".").generate_tokens()))
    print(list(Lexer("(1234", decimal_separator=".").generate_tokens()))
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

    # print(evaluate(
    #    "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((.))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"))

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


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
