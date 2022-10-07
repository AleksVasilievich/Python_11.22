# num = 12345
# while num != 0:
#     last_digit = num % 10
#     num =  num // 10
#     print(last_digit, end='')

# num = 5678
# num_clon = num
# sum_num = 0
# counter = 0
# mult_num = 1
# average = 0
# last_num = 0
# while num != 0:
#     last_digit = num % 10
#     sum_num += last_digit
#     counter += 1
#     mult_num *= last_digit
#     average = sum_num / counter
#     first_num = 0
#     num = num // 10
# print(sum_num)                    #  Сумма
# print(counter)                    #  Количество
# print(mult_num)                   #  Произведение
# print(average)                    #  Среднее арефметическое
# print(last_digit)                 #  Первая цивра
# print(last_digit + num_clon % 10) #  Сумма первой и последней цифры


num = int(input())
flage = True
while num > 0 and num // 10 != 0:
    num1 = num % 10
    num = num // 10
    if num != 0:
        num2 = num % 10
    if num1 > num2 :
        flage = False
if flage == True:
    print('YES')
else:
    print('NO')
