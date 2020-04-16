import subprocess
import traceback

if __name__ == "__main__":
    cmd = 'pipenv run datafaker rdb mysql+mysqldb://root:root@localhost:3306/demo?charset=utf8 user 10000 --meta meta.txt'
    for i in range(100):
        try:
            ret = subprocess.call('cmd', shell=False)
            print(ret)
        except Exception as e:
            print(traceback.format_exc())
            print(e)

# pipenv run datafaker rdb mysql+mysqldb://root:root@localhost:3306/demo?charset=utf8 user 10 --meta meta.txt
