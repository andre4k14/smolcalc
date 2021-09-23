import sys
import signal
from smolcalc.calculator import calculator


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def main():
    print(calculator("10+5"))
    #print(calculator(" 10^(50)"))
    #print(calculator("10+5.1"))
    #print(calculator("0^0"))
    #print(calculator("1234"))
    #print(calculator("10*"))



if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
