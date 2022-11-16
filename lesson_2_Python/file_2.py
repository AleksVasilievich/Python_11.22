# Чтение данных

with open('lesson_2_Python/file_txt.txt', 'r', encoding='utf-8') as data:
    for i in data:
        print(i)