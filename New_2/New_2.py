# a = float(input())
# b = float(input())
# c = float(input())
# d = (b * b) - (4 * a * c)
# if d > 0:
#     print(((-b) - (d ** 0.5)) / (2 * a))
#     print(((-b) + (d ** 0.5)) / (2 * a))
# elif d == 0:
#     print((-b) / (2 * a))
# elif d < 0:
#     print()
#     print('Нет корней')

# s = input()
# num = 0
# sum = 0
# while s != 'стоп' and s != 'хватит' and s != 'достаточно':
#     s = input()
#     num += 1
# print(num)

# n = int(input())
# while n % 7 == 0:
#     print(n)
#     n = int(input())
    
# n = int(input())
# count = 0
# while n >= 0:
#     count += n
#     n = int(input())
# print(count)  

# n = int(input())
# sum = 0
# while  n > 25:
#     n = n // 25
#     sum += n
# print(sum)

n = int(input())
sum = 0
num = 0
while n >= 25:
    num = n // 25
    n = n - 25 * num
    sum += num
while n >= 10:
    num = n // 10
    n = n - 10 * num
    sum += num
while n >= 5:
    num = n // 5
    n = n - 5 * num
    sum += num
while n >= 1:
    num = n // 1
    n = n - 1 * num
    sum += num
print(sum)
        