import logging

logging.basicConfig(
    filename='function.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s - Аргументы: %(args)s, Ключевые аргументы: %(kwargs)s - Результат: %(result)s'
)

def log_function_call(func):
    def wrapper(*args, **kwargs):
        logging.info(
            'Вызов функции',
            extra={
                'funcName': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': None
            }
        )
        try:
            result = func(*args, **kwargs)
            logging.info(
                'Результат функции',
                extra={
                    'funcName': func.__name__,
                    'args': args,
                    'kwargs': kwargs,
                    'result': result
                }
            )
            return result
        except Exception as e:
            logging.error(
                'Исключение в функции',
                extra={
                    'funcName': func.__name__,
                    'args': args,
                    'kwargs': kwargs,
                    'result': str(e)
                }
            )
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
