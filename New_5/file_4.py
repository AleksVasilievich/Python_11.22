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




s = [input() for _ in range(int(input()))]
ls = input() 
# print(*[s[i] for i in range(len(s)) if s[i].lower().find(ls.lower()) != -1], sep="\n")
print(*[i for i in s if ls.lower() in i.lower()], sep="\n")