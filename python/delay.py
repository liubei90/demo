import sys
import time


if __name__ == "__main__":
    print(f'sleep start')
    time.sleep(int(sys.argv[1]) or 1)
    print(f'sleep {sys.argv[1]}s')
