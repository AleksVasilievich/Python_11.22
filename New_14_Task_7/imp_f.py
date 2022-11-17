from importlib.resources import path


def imp():
    path = 'New_14_Task_7/ponebook.txt'
    data = open(path, 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()