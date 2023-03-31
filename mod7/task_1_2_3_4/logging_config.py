import sys

from handler import *
dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "'%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'"
        }
    },
    "handlers": {
        "custom_handlers": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stdout
            },
        "multi_file_handler":{
            "()": MultiFileHandler,
            "level": "DEBUG",
            "formatter": "base"
        }
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["custom_handlers","multi_file_handler"]
        }
    },
}