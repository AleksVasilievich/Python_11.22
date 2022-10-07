# num = 3
# produkt = 0
# for i in range(1, num + 1):         #   номер 1 task 1
#     total = 1
#     for j in range(1, i + 1):
#         total *= j
#     produkt += total
# print(produkt)


# import math

# num = 20
# total = 0

# for i in range(1, num + 1):          # namber  2  task 1
#     total += math.factorial(i)

# print(total)


# n = 10; a = 1; b = 0

# for i in range(1, n + 1):            # namder 3   task 1
#     a *= i
#     b += a

# print(b)


a = 2; b = 15
couter = 0
for i in range(a, b + 1):
    couter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            couter += 1
    if couter <= 2 and i != 1:
        print(i)
        
    