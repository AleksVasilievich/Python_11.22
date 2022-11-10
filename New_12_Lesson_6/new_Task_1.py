# Напишите программу вычисления арифметического выражения заданного строкой .
# Пример ->   2+2 => 4
# * Добавьте вожможность использования скобок.


def line(st):
    data1 = []
    a = ''
    for j in st:
        if j.isdigit():
            a += j
        else:
            data1.append(float(a))
            data1.append(j)
            a = ''
    data1.append(float(a))    
    return data1


def calaulate(data):
    result = 0
    while len(data) != 1:

        while '*' in data:
            index = data.index('*')
            result = data[index - 1] * data[index + 1]
            data = data[:index - 1] + data[index + 2:]
            data.insert(index - 1, result)
            break

        while '/' in data:
            index = data.index('/')
            result = data[index - 1] / data[index + 1]
            data = data[:index - 1] + data[index + 2:]
            data.insert(index - 1, result)
            break

        while '+' in data:
            index = data.index('+')
            result = data[index - 1] + data[index + 1]
            data = data[:index - 1] + data[index + 2:]
            data.insert(index - 1, result)
            break

        while '-' in data:
            index = data.index('-')
            result = data[index - 1] - data[index + 1]
            data = data[:index - 1] + data[index + 2:]
            data.insert(index - 1, result)
            break
    return data

st = '21+3*2+8/2-7'
line(st)
calaulate(data1)
# print(*data1)
# print(calaulate(data1))