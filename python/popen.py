import subprocess
import sys
import io


def main():
    print('111')
    p = subprocess.Popen("python delay.py 2", shell=True)
    print('222')
    p.wait()

    print('333')

def main2():
    print('111')
    # subprocess.call('python delay.py 2', shell=True)
    subprocess.run('python delay.py 2', shell=True)
    print('222')


def main3():
    errio = io.StringIO()
    subprocess.run('python raiseerr.py', shell=True, stderr=errio, stdout=errio)
    print('111', errio.getvalue())
    # try:
    #     errio = io.StringIO()
    #     subprocess.run('python raiseerr.py', shell=True, stderr=errio, stdout=errio)
    #     print('111', errio.getvalue())
    # except Exception as e:
    #     print('i'*12)
    #     print(sys.exc_info())

if __name__ == "__main__":
    print(sys.argv)
    main3()
