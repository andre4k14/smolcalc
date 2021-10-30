import sys
import signal
from smolcalc.calculator import evaluate, evaluate_all

sys.setrecursionlimit(5000)


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def main():
    print(evaluate([0, 0]))
    print(evaluate(None))
    print(evaluate("(((2+3)*(6-5))^((-pi)*23-(43*0.5)+6)*7)"))
    print(evaluate("ln(-12)"))
    print(evaluate(" 10^(50)"))
    print(evaluate("10+5.1"))
    print(evaluate("0^0"))
    print(evaluate("1234"))
    print(evaluate(
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((.))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"))

    print(evaluate(f"100_000"))
    print(evaluate("1+2*6/67"))
    print(evaluate("sdfask"))
    print(evaluate(f"10.1sqrt"))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
