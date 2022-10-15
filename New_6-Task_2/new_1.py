# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# print([i for i in range(int(input())) ])

# counter = 1
# n = int(input())
# ls = list(range(n))
# for i in ls:
#     counter *= i + 1
#     print(counter)


#  Задайте список. Напишите программу , которая определит, присутствует ли
#  в заданном списке строкнекое число.

# n = input()
# flag = 0
# ls = ['list 1', 'list 2', 'list 5']
# for i in ls:
#     if n in i:
#         flag += 1
# print('YES' if flag > 0 else 'NO')
        
#  Напишите прошрамму , которая определяет позицию второго вхождения 
# строки в списке , либо сообщает что её нет.

# count = 0
# count1 = 0
# ls = ['abc', 'qwe', 'zxc', 'qaz', 'abc', 'ert']
# for i in ls:
#     count1 += 1
#     if i == 'abc':
#         count += 1
#         if count == 2:
#             print(count1)
# if count != 2:
#     print('NO')


#   Реализуйте алгоритм задания случайных чисел
#  без встроенного генератора псевдослучайных чисел.

# import time

# t = 0
# while t <= 50 or t > 100:
#     t = int((time.time() - int(time.time())) * 1000)
# print(t)