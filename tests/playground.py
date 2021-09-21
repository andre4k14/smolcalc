import sys
import signal
from smolcalc.calculator import calculator


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def main():
    print(type(calculator("10+5")))
    print(calculator("10+5"))
    print(type(calculator("10+5.1")))
    print(calculator("10+5.1"))
    print(type(calculator("-.")))
    print(calculator("10*"))



if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
