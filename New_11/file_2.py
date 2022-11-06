
# n = []
# for i in input():
#     if ord(i) < 58 and ord(i) > 47:
#         n.append(i)
#         print(i, end='')
#     # print(ord(i))


# ls = ''.join(list(filter(lambda x: (ord(x) < 58 and ord(x) > 47), input())))
# #res = []
# for i in range(int(ls)):
#     st_1 = input()
#     for j in st_1:
#         if j == '#':
#             break
#         print(j, end='')
#     print()


       #res.append(j)
    #res.append('\n')
#res_1 = ''.join(res)    
#print(res_1.rstrip())    
    
#print(''.join(res))


# _________________________________________________________

# nam = list(map(int, input().split()))
# nam.sort()
# print(*nam)
# nam.sort(reverse = True)
# print(*nam)

# chars = [c for c in 'abcdefg']
# print(chars)
#--------------------------------------------------------------------
# palindromes = [i for i in range(100, 1000) if str(i)[0] == str(i)[2]]
# # palindromes = [i for i in range(100, 1000) if i % 10 == i // 100]\
# print(palindromes)      # Полиндром!
#------------------------------------------------------------------------
##################
# print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')
# # ------
# [print(_**2) for _ in range(1, int(input())+1)]
# # ------
# for j in [i**2 for i in range(1, int(input())+1)]: print(j)
# # ------\\\ ///
# ls = [i ** 2 for i in range(1, int(input()) + 1)]
# for j in ls:
#     print(j)
####################


# print(pow(3, 3))

# print(*[ pow(int(i), 3) for i in input().split()])

# print(*[i for i in input().split()], sep='\n')

