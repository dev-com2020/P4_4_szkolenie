import logging
from logging import config

config.dictConfig({
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s %(name)-12s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'filename': 'debug.log',
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
        },
        'stream': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'stream'],
            'level': 'DEBUG'
        },
    },
})

log_format = '%(levelname)-8s %(name)-12s %(message)s'

logging.basicConfig(
    filename='debug.log',
    format=log_format,
    level=logging.DEBUG
)

formatter = logging.Formatter(log_format)
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

logging.debug('debug')
logging.info('info')
some_logger = logging.getLogger('some')
some_logger.warning('warning')
some_logger.error('error')
other_logger = some_logger.getChild('other')
other_logger.critical('critical')
