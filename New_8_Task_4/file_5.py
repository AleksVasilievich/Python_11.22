# with open('New_8_Task_4\line_1.txt', 'r', encoding='utf_8') as data:
#     data1 = list(map(str, data.readline().split(',')))
#     print(data1)

# with open('New_8_Task_4\line_2.txt', 'r', encoding='utf_8') as data:
#     data2 = list(map(str, data.readline().split(',')))
#     print(data2)


# a = [1, 2, -5, 0, 5, 10]
# b = sorted(a)
# print(b[:3])
# print(a)

# digs = (-10, 0, 7, -2, 3, 6, -8)
# print(sorted(digs, key = lambda x: x >= 0))
# print(sorted(digs))



# print(sorted({'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}, key = lambda x: x[0], reverse=True))

# ls = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
# print(sorted(ls, key = lambda x: chr(x[0])))

#######################################################################
# На вход программе подается строка текста. Напишите программу, 
# которая подсчитывает количество цифр в данной строке.

# ls = ' '.join(input())
# total = 0
# for i in ls:
#     if ord(i) > 47 and ord(i) < 58:
#         total += 1
# print(total)


# k = 0
# for i in input():
#     if '0'<= i <= '9':
#         k += 1
# print(k)

# print(sum(i.isdigit() for i in input()))

# sam = 0
# for i in input():
#     sam += i.isdigit()
# print(sam)


# print(len([i for i in input() if i.isdigit()]))

#################################################################################