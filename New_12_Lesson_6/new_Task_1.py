# Напишите программу вычисления арифметического выражения заданного строкой .
# Пример ->   2+2 => 4
# * Добавьте вожможность использования скобок.

data1 = '2+3*2+8/2-2'
data = []
for j in data1:
    if j.isdigit():
        data.append(int(j))
    else:
        data.append(j)
print(data)

result = 0

while '*' in data:
    index = data.index('*')
    result = data[index - 1] * data[index + 1]
    data = data[:index - 1] + data[index + 2:]
    data.insert(index - 1, result)
    print(result)
    break
print(data)






# for i in data:
#     while i == '*':
#         # ls = float(data[data.index('*') - 1]) * float(data[data.index('*') + 1])
#         data = data[:data.index('*') - 1] + str(float(data[data.index('*') - 1]) * float(data[data.index('*') + 1])) + data[data.index('*') + 2:]
#         print(data)
#         break
# for i in data:    
#     while i == '/':
#         data = data[:data.index('/') - 1] + str(float(data[data.index('/') - 1]) / float(data[data.index('/') + 1])) + data[data.index('/') + 2:]
#         print(data)
#         break
# for i in data:    
#     while i == '+':
#         data = data[:data.index('+') - 1] + str(float(data[data.index('+') - 1]) + float(data[data.index('+') + 1])) + data[data.index('+') + 2:]
#         print(data)
#         break
# for i in data:    
#     while i == '-':
#         data = data[:data.index('-') - 1] + str(float(data[data.index('-') - 1]) / float(data[data.index('-') + 1])) + data[data.index('-') + 2:]
#         print(data)
#         break