import logging.config

from Exercise.M_LOG.conf.setting import LOGGIN_DIC

print(LOGGIN_DIC)
logging.config.dictConfig(LOGGIN_DIC)

def getLogger(name):
    return logging.getLogger(name)
