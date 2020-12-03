import logging
import sys
import module1.log1
import module1.module3.log3


def test1():
    # 将root的handler设置为NullHandler，将会屏蔽root向控制台输出内容
    logging.basicConfig(level=logging.DEBUG, handlers=[logging.FileHandler('log.txt', mode='a', encoding='utf8')])
    # logging.basicConfig(level=logging.DEBUG)
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')


    # mlog设置自己的handler为StreamHandler，将日志输出到控制台
    # mlog = logging.getLogger('mlog')
    # mlog.setLevel(logging.DEBUG)
    # sh = logging.StreamHandler(sys.stdout)
    # sh.setFormatter(logging.Formatter('mlog: %(message)s'))
    # mlog.addHandler(sh)
    # mlog.debug('debug')
    # mlog.info('info')
    # mlog.warning('warning')
    # mlog.error('error')


    # 模块中的log没有设置自己的handler，会使用root的NullHandler，导致日志不会输出到控制台
    # module1.log1.do_log()
    # module1.module3.log3.do_log()


def test2():
    # 将root的level设置为WARNING， 只会输出warning error
    logging.basicConfig(level=logging.WARNING)
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')

    # 将mlog的level设置为INFO， 会输出info warning error， 同时使用root的handler输出info warning error
    mlog = logging.getLogger('mlog')
    mlog.propagate = False
    mlog.setLevel(logging.INFO)
    # sh = logging.StreamHandler(sys.stdout)
    sh = logging.FileHandler('log.txt', mode='a', encoding='utf8')
    sh.setFormatter(logging.Formatter('mlog: %(message)s'))
    mlog.addHandler(sh)
    mlog.debug('debug')
    mlog.info('info')
    mlog.warning('warning')
    mlog.error('error')

def test3():
    # 将root的level设置为WARNING， 只会输出warning error
    logging.basicConfig(level=logging.WARNING, format='123  %(message)s')
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')

    # 将mlog的level设置为INFO， 会输出info warning error， 同时使用root的handler输出info warning error
    mlog = logging.getLogger('mlog')
    mlog.setLevel(logging.INFO)
    mlog.propagate = False
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(logging.Formatter('mlog: %(message)s'))
    mlog.addHandler(sh)
    mlog.debug('debug')
    mlog.info('info')
    mlog.warning('warning')
    mlog.error('error')


if __name__ == "__main__":
    test1()