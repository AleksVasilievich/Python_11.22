# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить 
# в нем только двузначные числа.Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел 
# в одну строчку через пробел.     [1,2,3,4,22,234,24] ----> [22, 24]


print(list(map(int, filter(lambda i: len(i) == 2, input().split()))))