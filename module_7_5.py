import os
import time
main_path = os.getcwd()
for root, dirs, files in os.walk('.'):
    root = root[2:]
    for file in files:
        if os.path.isfile(file):
            filepath = os.path.join(main_path, root, file)
            filetime = os.path.getmtime(file)
            formatted_time = time.ctime(filetime)
            filesize = os.stat(file).st_size
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
                  f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
