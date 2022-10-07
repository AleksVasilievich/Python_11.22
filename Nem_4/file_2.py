# num = int(input())

# langs = list()
# total = 0
# while total < num:
#     s = input()
#     langs.append(s)
#     total += 1

# print(langs)



# alf = list()
# num = list()
# total = 1
# for i in range(26):
#     num.append(chr(i + 97) * total)
#     total += 1
# print(num)



# n = int(input())
# nambers = list()
# total = 0
# while total < n:
#     num = input()
#     nambers.append(pow(int(num), 3))
#     total += 1
# print(nambers)



# n = int(input())
# num = list()

# for i in range(n):
#     if n % (i + 1) == 0:
#         num.append(i + 1)
# print(num)



# n = int(input())
# line = list()
# line1 = list()
# for i in range(n):
#     num = int(input())
#     line.append(num)
#     if i > 0:
#         line1.append(sum(line))
#         del line[0]
# print(line1)        



# n = int(input())
# line = list()
# line1 = list()
# for i in range(n):
#     num = int(input())
#     line.append(num)
# del line[1::2]
# print(line)


# n = int(input())
# k = int(input())

# for i in range(n):
#     s = input()
#     line.append(s[k - 1])
# print(line)


# line = list()
# line1 = ''
# n = int(input())
# for i in range(n):
#     s = input()
#     line.append(s)

# k = int(input())
# for j in range(n):
#     if len(line[j]) > k - 1:
#         line1 += line[j][k - 1]
# print(line1)


# data = [input() for i in range(int(input()))]
# k = int(input())
# for i in data:
#     if len(i) >= k:
#         print(i[k - 1], end='')


# strings = [list(input()) for _ in range(int(input()))]
# k = int(input()) - 1
# print(*[s[k] for s in strings if k < len(s)], sep='')       


# line = [input() for i in range(int(input()))]
# print(line)

n = int(input())
line = []
for i in range(n):
    s = input()
    line.extend(s)
print(line)