import sys
import signal
import cProfile
import pstats
import test
import unittest

from smolcalc import evaluate

def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)

def test_speed():
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner().run(suite)





def main():
    with cProfile.Profile() as pr:
        test_speed()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

    stats.dump_stats(filename="speed_text.prof")





if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
