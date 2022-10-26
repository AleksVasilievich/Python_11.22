# 2) Создайте программу для игры в ""Крестики-нолики"".

# list = [["","",""], ["","",""], ["","","*"]]
# for i in range(9):
# if i % 2 == 0:
# print("1 игрок")
# Ввод: 3 2
# if i % 2 == 1:
# print("2 игрок")


line = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

for i in line:
    print(*i)

pl_1 = '0'
pl_2 = 'x'
for n in range(9):
    if n % 2 == 0:
        print("1 игрок")
        pl = pl_1

        m = input('Введите номер ячейки -> ')
        k_v = 0
        k_s = 0
        for i in line:
            for j in i:
                if j == m:
                    k_v += int(j) - 1
                    line[k_s][k_v] = pl
            k_s += 1
            k_v -= 3

        for i in line:
            print(*i)                                           

        if line[0][0] == line[0][1] == line[0][2] or line[1][0] == line[1][1] == line[1][2] or line[2][0] == line[2][1] == line[2][2]\
                or line[0][0] == line[1][0] == line[2][0] or line[0][1] == line[1][2] == line[2][1] or line[0][2] == line[1][2] == line[2][2]\
                or line[0][0] == line[1][2] == line[2][2] or line[0][2] == line[1][2] == line[2][0]:
            print('Выиграл 1 игрок !')
            break    

    if n % 2 == 1:
        print("2 игрок")
        pl = pl_2 

        m = input('Введите номер ячейки -> ') 
        k_v = 0
        k_s = 0
        for i in line:
            for j in i:
                if j == m:
                    k_v += int(j) - 1
                    line[k_s][k_v] = pl
            k_s += 1
            k_v -= 3

        for i in line:
            print(*i)

        if line[0][0] == line[0][1] == line[0][2] or line[1][0] == line[1][1] == line[1][2] or line[2][0] == line[2][1] == line[2][2]\
                or line[0][0] == line[1][0] == line[2][0] or line[0][1] == line[1][2] == line[2][1] or line[0][2] == line[1][2] == line[2][2]\
                or line[0][0] == line[1][2] == line[2][2] or line[0][2] == line[1][2] == line[2][0]:
            print('Выиграл 2 игрок !')
            break
       
print('Ничья !')