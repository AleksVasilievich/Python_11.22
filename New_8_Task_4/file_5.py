with open('New_8_Task_4\line_1.txt', 'r', encoding='utf_8') as data:
    data1 = list(map(str, data.readline().split(',')))
    print(data1)

with open('New_8_Task_4\line_2.txt', 'r', encoding='utf_8') as data:
    data2 = list(map(str, data.readline().split(',')))
    print(data2)

