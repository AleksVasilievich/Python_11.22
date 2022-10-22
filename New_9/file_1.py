# # Рекурсия : Нахождение чисел Фибоначи.

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# ls = []
# for e in range(1, 10):
#     ls .append(fib(e))
# print(ls)

# ______________________________________________________

# def f(x):
#     return x * x

# ls1 = [1, 2, 3, 5, 8, 15, 23, 38]
# print(*[(i, f(i)) for i in ls1 if i % 2 == 0])


data = list(map(int, '1,2,3,456,56'.split(',')))
print(data)
