import random

_CONFIG = None

def init_config():
    global _CONFIG
    if random.random() > 0.5:
        _CONFIG = True
    else:
        _CONFIG = False

def get_config():
    return _CONFIG