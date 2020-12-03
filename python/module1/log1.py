import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, handlers=[logging.FileHandler('log1.txt', mode='a', encoding='utf8')])

def do_log():
    log.info('do log in log1')
    logging.info('sss')