import subprocess


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


if __name__ == "__main__":
    main2()
