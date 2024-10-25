import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(root)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
