# Запись  данных

with open('lesson_2_Python/file_txt.txt', 'a', encoding='utf-8') as data:
    # data.write('New file-1\n')
    # data.write('New file-2\n')
    data.writelines(input(' Введите данные '))
    data.writelines(' ')