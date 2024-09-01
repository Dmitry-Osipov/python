import logging

logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        logging.error("Произошла ошибка деления на ноль: %s", e)
        return None

numerator = 10
denominator = 0

result = divide(numerator, denominator)
if result is None:
    print("Ошибка деления на ноль. Проверьте файл error.log для получения дополнительной информации.")
else:
    print(f"Результат деления: {result}")
