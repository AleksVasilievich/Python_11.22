# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:    - 6782 -> 23      - 0, 56 -> 11

print(sum([int(i) for i in str(input()) if str(i) != '.' and str(i) != '-']))

# ls = 0.345
# res = []
# for i in str(ls):
#     if str(i) != '.':
#         res.append(int(i))
# print(sum(res))   

