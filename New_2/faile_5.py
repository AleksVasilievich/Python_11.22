# n = 5
# for j in range(1, n + 1):
#     for i in range(1, j + 1):
#         print(i, end='')
#     for k in range(j - 1, 0, - 1):
#         print(k, end='')
#     print()




# n = 5
# p = 0
# for i in range(n):
#     while p < n:
#         print(p + 1, end=' ')
#         p += 1
#         while p >= n:
#             print(p - 1, end=' ')
#             p -= 1


# n, m = 1, 100
# sam, sam1, num = 0, 0, 0
# for i in range(n, m + 1):
#     for j in range(1,m + 1):
#         if i % j == 0:
#             sam += j
#             if sam >= sam1:
#                 sam1 = sam
#                 num = j
#     sam = 0
# print(num, sam1)

# a , b = 1, 100
# total_maximum = 0
# digit = 0

# for i in range(a, b + 1):
#     maximum = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             maximum += j
#         if maximum > total_maximum:
#             total_maximum = maximum
#             digit = j
# print(digit, total_maximum)

# n = 5
# for i in range(1, n + 1):
#     d = 0
#     for j in range(1, n + 1):
#         if i % j == 0:
#             d += 1
#     print(i, d * '+', sep='')

# n = 192
# total = 0
# final_n = 0

# while n != 0:
#     final_n = n % 10
#     total += final_n
#     n = n // 10

# while total != 0:
#     final_n = total % 10
#     n += final_n
#     total = total // 10

# while n % 10 != 0:
#     final_n = n % 10
#     total += final_n
#     n = n // 10
# n = total    

# print(n)     

number = 192

total = 0

while number > 9:  
    while number != 0:
        total += number % 10
        number //= 10
    number, total = total, 0

print(number)

