# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sam = 0
# for nam in numbers:
#     sam = sam + nam * nam
# print(sam)


# num = []
# for i in range(int(input())):
#     num.append(int(input()))
# print(*num, sep='\n')
# print()





# for num1 in num:
#     num1 = num1 * num1 + 2 * num1 + 1
#     print(num1)



# l = []
# for i in range(int(input())):
#     i = (int(input()))
#     print(i)
#     l.append(i**2+2*i+1)
# print()
# print(*l, sep='\n')




# line = []
# for i in range(int(input())):
#     i = int(input())
#     line.append(i)
# line.remove(max(line))
# line.remove(min(line))
# print(*line, sep='\n')


# ls = [int(input()) for _ in range(int(input()))]
# [print(i) for i in ls if i not in (max(ls), min(ls))]





# ls = [input() for _ in range(int(input()))]
# ls.reverse()
# for i in ls:
#     if ls.count(i) > 1:
#         ls.remove(i)
# ls.reverse()
# print(*ls, sep='\n')


# n = int(input())
# ass = []
# for i in range(n):
#     dick = input()
#     if dick not in ass:
#         ass.append(dick)
# print(*ass, sep='\n')


# s = [input() for _ in range(int(input()))]
# print(*[s[i] for i in range(len(s)) if s[:i].count(s[i]) == 0], sep="\n")




# s = [input() for _ in range(int(input()))]
# ls = input() 
# # print(*[s[i] for i in range(len(s)) if s[i].lower().find(ls.lower()) != -1], sep="\n")
# print(*[i for i in s if ls.lower() in i.lower()], sep="\n")



# s = [input() for _ in range(int(input()))]
# k = [input() for _ in range(int(input()))]
# counter = 0
# for i in s:
#     for j in k:
#         counter = 0
#         if j.lower() in i.lower():
#             counter += 1
#             if counter >= len(k):
#                 print(i, sep='\n')


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# s = [[input() for _ in range(int(input()))] for _ in '01']
# print(* [i for i in s[0] if all(j.lower() in i.lower() for j in s[1])], sep='\n')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# ls = [input() for _ in range(int(input()))]


# ls = [-7, 0, -19, 3, 0, 1, -32]
# print(*(sorted(ls)), sep='\n')

# ______________________________________

x = [int(input()) for _ in range(int(input()))]
print(*[i for i in x if i < 0], *[i for i in x if i == 0], *[i for i in x if i > 0], sep = '\n')


print(*sorted([int(input()) for _ in range(int(input()))], key = lambda x: abs(x) / x if x != 0 else 0), sep='\n')


lst = [int(input()) for i in range(int(input()))]
[print(i) for i in lst if i < 0]
[print(i) for i in lst if i == 0]
[print(i) for i in lst if i > 0]

# _____________________________________