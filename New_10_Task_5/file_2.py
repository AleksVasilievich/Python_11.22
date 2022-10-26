# 2) Создайте программу для игры в ""Крестики-нолики"".

# list = [["","",""], ["","",""], ["","","*"]]
# for i in range(9):
# if i % 2 == 0:
# print("1 игрок")
# Ввод: 3 2
# if i % 2 == 1:
# print("2 игрок")


line = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

pl_1 = '0'
pl_2 = 'x'
for i in range(9):
    if i % 2 == 0:
        print("1 игрок")
        pl = pl_1 
    elif i % 2 == 1:
        print("2 игрок")
        pl = pl_2


def intp(x, list):

    m = input()
    k_v = 0
    k_s = 0
    for i in line:
        for j in i:
            if j == m:
                k_v += int(j) - 1
                line[k_s][k_v] = pl
        k_s += 1
        k_v -= 3
    return line    

intp(x, line)

for i in line:
    print(*i)