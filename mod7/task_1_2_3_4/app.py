import logging.config

from util import *
from handler import *
from logging_config import dict_config
logging.config.dictConfig(dict_config)
logger = logging.getLogger('module_logger.app')

# получаем первое число
num1 = (input("Введите первое число: "))
# получаем второе число
num2 = (input("Введите второе число: "))
if not(num1.isdigit()):
    logger.error(f"num1({num1}) is not number")
    exit()
if not (num2.isdigit()):
    logger.error(f"num2({num2}) is not number")
    exit()
result = calculate(float(num1),float(num2))
logger.warning('Warning message')
logger.critical('critical message')