import logging

logging.basicConfig(
    filename='function.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_function_call(func):
    def wrapper(*args, **kwargs):
        # Логируем аргументы функции
        logging.info(f"Вызов функции '{func.__name__}' с аргументами: {args} и {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Результат функции '{func.__name__}': {result}")
            return result
        except Exception as e:
            logging.error(f"Исключение в функции '{func.__name__}': {e}")
            raise
    return wrapper


@log_function_call
def divide(a, b):
    return a / b

numerator = 10
denominator = 2
divide(numerator, denominator)

numerator = 10
denominator = 0
try:
    divide(numerator, denominator)
except ZeroDivisionError:
    print("Произошла ошибка деления на ноль. Проверьте файл function.log для получения дополнительной информации.")
