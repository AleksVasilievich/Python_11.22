# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# mn = 0
# s = 0
# for i in range(1, 11):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x > mn:
#         mn = x
# if s < 0:
#     print()
#     print(s)
#     print(mn)
# else:
#     print('NO')

# s = 0
# for i in range(3):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)

# n = int(input())
# max_digit = 0
# while n > 0:
#     n = n % 10
#     if n % 3 == 0:
#         if n > max_digit:
#             max_digit = n
#     n = n // 10
# if max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# n2 = 0
# while n > 0:
#     n2 = n % 10
#     n = n // 10
# print(n2)

# n = 3
# m = 0
# for i in range(n):
#     if i <= n // 2:
#         m = m + 1
#     else:
#         m = m - 1
#     for j in range(m):
#         print('*', end='')
#     print()

# n = 7
# for i in range(1, n + 1):
#     print('*' * min(i, n - i + 1))


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()


# total = 0
# for b in range(1, 11):
#     for k in range(1, 21):
#         for t in range(1, 201):
#             if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
#                 total += 1
#                 print('b =', b, 'k =', k, 't =', t)
# print('Общее количество натуральных решений =', total)

# n = 3
# total = 1
# for i in range(1, n + 1):   
#     for j in range(i):
#         print(total, end='')
#         total += 1
#     print()


# n = 14
# s = 'f'
# for i in s:
#     if ord(i) - n < 97:
#         print(chr(ord(i) - n + 26))
#     else:
#         print(chr(ord(i) - n))