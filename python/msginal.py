import signal, os, time

def inthandler(signum, frame):
    '''
    信号量优先级会高于sleep, 导致上次的sleep失效
    '''
    print('inthandler')
    print(signum)
    print(frame)
    time.sleep(5)
    print('inthandler end')
    exit(1)

signal.signal(signal.SIGINT, inthandler)

def main():
    while True:
        time.sleep(1)
        print('---')


if __name__ == "__main__":
    main()
