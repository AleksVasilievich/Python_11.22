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


# data = list(map(int, '1,2,3,456,56'.split(',')))
# print(data)


# print('YES' if input().endswith(('.com','.ru')) else 'NO')


###########################################
# ls = 'jfsdjlkpppppjf'
# total = 0
# ls_i = ''
# for i in ls:
#     if ls.count(i) >= total:
#         total = ls.count(i)
#         ls_i = i
# print(ls_i)


# ls = 'jfsdjlkpppppjf'[::-1]
# print(max(ls, key = ls.count))

# ###################################################     

# ls = 'abcdeghabc'
# n = ls.find('f')
# m = ls.rfind('f')
# if n != m:
#     print(n, m, end='')
# elif n == - 1:
#     print('NO')
# else:
#     print(n)

#########################

# ls = 'ahbhchdeghahbhc'
# n = ls.find('h')
# m = ls.rfind('h')
# ls_1 = ls[:n]
# ls_2 = ls[m + 1:]
# print(ls_1, end='' )
# print(ls_2)
# ______________________________
# if n != m:
#     print(n, m, end='')
# elif n == - 1:
#     print('NO')
# else:
#     print(n)



# numbers = [8, 9, 10, 11]
# nambers[1] = 17
# # nambers.append(4)
# # nambers.append(5)
# # nambers.append(6)
# # nambers.remove(8)
# # nambers *= nambers
# # nambers.append(25,3)
# print(nambers)


