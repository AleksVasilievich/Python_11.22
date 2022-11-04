
# n = []
# for i in input():
#     if ord(i) < 58 and ord(i) > 47:
#         n.append(i)
#         print(i, end='')
#     # print(ord(i))


ls = ''.join(list(filter(lambda x: (ord(x) < 58 and ord(x) > 47), input())))
for i in range(int(ls)):
    st_1 = input()
    for j in st_1:
        while j != '#':
            print(j)


# print(ls)