import argparse
import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

logging.basicConfig(
    filename='directory_contents.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s' 
)

def gather_directory_info(directory_path):
    """Собирает информацию о содержимом указанной директории и возвращает список объектов FileInfo."""
    file_info_list = []
    
    try:
        if not os.path.isdir(directory_path):
            raise ValueError(f"{directory_path} не является директорией.")
        
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            parent_directory = os.path.basename(directory_path)
            
            if os.path.isdir(full_path):
                file_info = FileInfo(name=entry, extension='', is_directory=True, parent_directory=parent_directory)
            else:
                name, extension = os.path.splitext(entry)
                file_info = FileInfo(name=name, extension=extension[1:], is_directory=False, parent_directory=parent_directory)
            
            file_info_list.append(file_info)
    
    except Exception as e:
        logging.error(f"Ошибка при обработке директории {directory_path}: {e}")
    
    return file_info_list

def log_directory_info(file_info_list):
    """Записывает информацию о файлах и каталогах в лог-файл."""
    for file_info in file_info_list:
        if file_info.is_directory:
            logging.info(f"Каталог: {file_info.name}, Родительский каталог: {file_info.parent_directory}")
        else:
            logging.info(f"Файл: {file_info.name}, Расширение: {file_info.extension}, Родительский каталог: {file_info.parent_directory}")

def main():
    parser = argparse.ArgumentParser(description="Сбор информации о содержимом директории.")
    parser.add_argument('directory', type=str, help="Путь до директории")
    
    args = parser.parse_args()
    
    file_info_list = gather_directory_info(args.directory)
    log_directory_info(file_info_list)
    
    print(f"Информация о содержимом директории записана в файл 'directory_contents.log'.")

if __name__ == "__main__":
    main()
