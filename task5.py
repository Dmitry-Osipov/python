import argparse
import logging
from datetime import datetime
import calendar

logging.basicConfig(
    filename='date_parser.log',  
    level=logging.ERROR,    
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def parse_date(day_number, weekday_name, month_name):
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

        if isinstance(month_name, int):
            month = month_name
        elif month_name in months:
            month = months[month_name]
        else:
            raise ValueError("Неизвестное название месяца")

        if isinstance(weekday_name, int):
            weekday = weekday_name
        elif weekday_name in weekdays:
            weekday = weekdays[weekday_name]
        else:
            raise ValueError("Неизвестное название дня недели")

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
        logging.error(f"Ошибка при разборе текста: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Преобразование текстового описания даты в дату текущего года.")
    parser.add_argument('--day', type=int, default=1, help="Номер дня (по умолчанию 1)")
    parser.add_argument('--weekday', type=int, default=datetime.now().weekday(), help="День недели (0-понедельник, 6-воскресенье, по умолчанию сегодня)")
    parser.add_argument('--month', type=int, default=datetime.now().month, help="Месяц (1-12, по умолчанию текущий месяц)")
    
    args = parser.parse_args()
    
    result = parse_date(args.day, args.weekday, args.month)
    if result:
        print(f"Дата для дня {args.day}, дня недели {args.weekday}, месяца {args.month}: {result.strftime('%d-%m-%Y')}")
    else:
        print(f"Не удалось найти дату. Проверьте файл date_parser.log для получения дополнительной информации.")

if __name__ == "__main__":
    main()
