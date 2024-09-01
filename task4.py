import logging
from datetime import datetime
import calendar

logging.basicConfig(
    filename='date_parser.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def parse_date(text):
    try:
        months = {
            'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5,
            'июня': 6, 'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10,
            'ноября': 11, 'декабря': 12
        }
        
        weekdays = {
            'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4,
            'суббота': 5, 'воскресенье': 6
        }

        parts = text.split()
        if len(parts) != 4:
            raise ValueError("Формат текста неверен")

        day_number = int(parts[0][:-1]) 
        weekday_name = parts[1]
        month_name = parts[3] 

        if month_name not in months:
            raise ValueError("Неизвестное название месяца")
        if weekday_name not in weekdays:
            raise ValueError("Неизвестное название дня недели")

        month = months[month_name]
        weekday = weekdays[weekday_name]
        year = datetime.now().year

        first_day_of_month = datetime(year, month, 1)
        
        day = 0
        for i in range(1, 32):
            try:
                candidate_date = datetime(year, month, i)
                if candidate_date.weekday() == weekday:
                    day += 1
                    if day == day_number:
                        return candidate_date
            except ValueError:
                break
        
        raise ValueError("Не удается найти требуемый день")

    except Exception as e:
        logging.error(f"Ошибка при разборе текста '{text}': {e}")
        return None

texts = [
    "1-й четверг ноября",
    "3-я среда мая",
    "2-я понедельник января"
]

for text in texts:
    result = parse_date(text)
    if result:
        print(f"Дата для '{text}': {result.strftime('%d-%m-%Y')}")
    else:
        print(f"Не удалось разобрать текст '{text}'. Проверьте файл date_parser.log для получения дополнительной информации.")
