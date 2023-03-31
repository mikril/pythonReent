import logging.config
from handler import *
from logging_config import dict_config

logging.config.dictConfig(dict_config)
logger = logging.getLogger('module_logger.util')


def calculate(num1,num2):


    # выводим меню операций
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Умножение")

    # получаем выбор пользователя
    choice = input("Введите номер операции (1/2): ")

    # вычисляем результат в зависимости от выбора пользователя
    if choice == '1':
        result = num1 + num2
        logger.debug(f"Calculation result of util({num1} + {num2}) = {result}")
    elif choice == '2':
        result = num1 * num2
        logger.debug(f"Calculation result of util({num1} * {num2}) = {result}")
    else:
        logger.error("Некорректный выбор операции")


    return result
    # выводим результат

