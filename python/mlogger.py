import logging
import sys
import module1.log1
import module1.module3.log3


# 将root的handler设置为NullHandler，将会屏蔽root向控制台输出内容
logging.basicConfig(level=logging.DEBUG, handlers=[logging.NullHandler()])
# logging.basicConfig(level=logging.DEBUG)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')


# mlog设置自己的handler为StreamHandler，将日志输出到控制台
mlog = logging.getLogger('mlog')
mlog.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(logging.Formatter('mlog: %(message)s'))
mlog.addHandler(sh)
mlog.debug('debug')
mlog.info('info')
mlog.warning('warning')
mlog.error('error')


# 模块中的log没有设置自己的handler，会使用root的NullHandler，导致日志不会输出到控制台
module1.log1.do_log()
module1.module3.log3.do_log()

