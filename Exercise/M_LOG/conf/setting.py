LOGGIN_DIC={
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'o_fmt1':{'format' : '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'},
        'o_fmt2':{'format':'%(asctime)s *** %(name)s *** %(msg)s'}
    },

    'filters':{},
    'handlers':{
        'o_hd_file': {
            'level':'WARNING',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter':'o_fmt1',
            'filename':'sys.log',
            'encoding':'utf-8',
            'maxBytes':1024*1024*5,
            'backupCount':5
        },

        'o_hd_cmd': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'o_fmt1'
        }
    },
    'loggers':{
        'o_owen':{
            'level':'DEBUG',
            'handlers':['o_hd_file','o_hd_cmd']
        },
        'o_zero':{
            'level': 'DEBUG',
            'handlers': [ 'o_hd_cmd']
        }
    }

}


# import logging.config
# logging.config.dictConfig(LOGGIN_DIC)
#
# log= logging.getLogger('o_owen')
# log.critical("hello")
# # log.critical("hello")s
