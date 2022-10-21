# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7 

# n = 8
# col = []
# for i in range(2, n + 1):
#     if n % i == 0:
#         count = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
#             if count > 2:
#                 break
#         if count == 2:
#             print(i, end='')
#             # print(col.append(i))



num = int(input('Введите число : '))
div = 2
col = []

while div <= num:
    if num % div == 0:
        col.append(div)
        num //= div
        div = 2
    else:
        div += 1   
print(col)         
