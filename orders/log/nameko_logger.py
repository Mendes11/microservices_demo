import os
import traceback
import logging
import logging.config
from nameko.extensions import DependencyProvider

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def logging_format(logger_name, log_level='INFO'):
    log_format = {
        'version': 1,
        'disable_existing_loggers': False,
        # How to format the output
        'formatters': {
            'standard': {
                'format':
                "[%(asctime)s] %(threadName)s - %(name)s - %(levelname)s :  %(message)s",
                'datefmt':
                "%d/%m/%Y %H:%M:%S"
            },
            'djangolog': {
                'format':
                    '[%(asctime)s] - %(name)s - %(message)s',
                'datefmt':
                    '%d/%m/%Y %H:%M:%S'
            },
        },
        # Log handlers (where to go)
        'handlers': {
            logger_name: {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': BASE_DIR + '/log/' + logger_name + '.log',
                'maxBytes': (1024 * 1024) * 2,
                'backupCount': 10,
                'formatter': 'djangolog'
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            logger_name: {
                'handlers': ['console', logger_name],
                'propagate': True,
                'level': log_level,
            },
        }
    }
    return log_format


class NamekoLogger(DependencyProvider):

    def worker_result(self, worker_ctx, result, exc_info):
        if exc_info is None:
            return

        log_format = logging_format(worker_ctx.service_name)
        logging.config.dictConfig(log_format)
        logger = logging.getLogger(worker_ctx.service_name)
        logger.exception('SERVICE NAME: {}\nTraceback (most recent call last):\n{}\n{}: {}'.format(worker_ctx.service_name,
                                                                           ''.join(traceback.format_tb(exc_info[2])),
                                                                           exc_info[0].__name__, exc_info[1]))


def get_logger(service_name, logger_level='INFO'):
    logging.config.dictConfig(logging_format(service_name,
                                             log_level=logger_level))
    logger = logging.getLogger(service_name)
    return logger
