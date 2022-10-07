# a = int(input())
# b = int(input())
# if a > b:
#     print(a + b)
# else:
#     print(a * b)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')


# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         sum += i
# print(sum)

# n = int(input())
# m1 = 0
# m2 = 0
# for i in range(n):
#     num = int(input())
#     if num > m2:
#         m2 = num
#         if m1 < m2:
#             m1 = m2
# print()
# print(m2)
# print(m1)

n = int(input())
a1 = 1
a2 = 0
b = 0
for i in range(1, n + 1):
    b = a1
    a1 = b + a2
    a2 = b
    
    print(b, end = '')
