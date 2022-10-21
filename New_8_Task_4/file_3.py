# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# 3 1 2 3      2 1

s = ''.join(input().split())
for i in range(len(s)):
    if s.count(s[i]) == 1:
        print(s[i], end='')














# s = [input() for _ in range(int(input()))]
# sam = 0
# for n in range(len(s)):
#     sl = s[n]
#     print(sl)
#     if sl.count('11') >= 3:
#         sam += 1
# print(sam)


# n = int(input())
# counter = 0
# for _ in range(n):
#     s = input()
#     if s.count('11') >= 3:
#         counter += 1
# print(counter)