# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# print([i for i in range(int(input())) ])

counter = 1
n = int(input())
ls = list(range(n))
for i in ls:
    counter *= i + 1
    print(counter)