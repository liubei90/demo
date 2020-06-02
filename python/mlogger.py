import logging
import sys


# logging.basicConfig(level=logging.DEBUG)
mlog = logging.getLogger('mlog')
# Logging默认是WARNING, 是所有handler的下限
mlog.setLevel(logging.DEBUG)

# 
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.ERROR)
mlog.addHandler(sh)

fh = logging.FileHandler('log.txt', mode='w')
fh.setLevel(logging.DEBUG)
mlog.addHandler(fh)

mlog.debug('debug')
mlog.info('info')
mlog.warning('warning')
mlog.error('error')
