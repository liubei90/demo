import time
class Test():
    def __init__(self):
        print('init')

    @property
    def _prop1(self):
        print('_prop1')
        return 1

    def get_prop1(self):
        return self._prop1

if __name__ == "__main__":
    t = Test()
    time.sleep(3)
    t.get_prop1()
