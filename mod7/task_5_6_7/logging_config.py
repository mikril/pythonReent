import string
import logging

class ASCIIFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        return str.isascii(msg)

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "'%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'"
        }
    },
    "handlers": {
        "file_log":{
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when":"s",
            "backupCount":1,
            "interval": 10,
            "level": "INFO",
            "formatter": "base",
            "filename": "utils.log",
            "filters": ["ascii_filter"]
        }
    },
    "filters": {
        "ascii_filter": {
            "()": ASCIIFilter
        }
    },
    "loggers": {
        "module_logger": {
            "level": "INFO",
            "handlers": ["file_log"]
        }
    },
}