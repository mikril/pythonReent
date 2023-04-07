
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
        },
        "server": {
            "class": "logging.handlers.HTTPHandler",
            "formatter": "base",
            "level": "DEBUG",
            "host": "localhost:5000",
            "url": "/save_log",
            "method": "POST",

        }
    },

    "loggers": {
        "module_logger": {
            "level": "INFO",
            "handlers": ["file_log","server"]
        }
    },
}