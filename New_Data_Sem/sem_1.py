# with open('New_Data_Sem\data.txt', 'r') as ls:
#     for ls1 in ls:
#         ls1 = list(ls1.split())
#         for i in ls1:
#             if int(i) != ls1.index(i) + 1:
#                 print(int(i) - 1)
#                 break
#     print(ls1)

#######################
#  Пример : 1 2 3 5 6 7
#  Вывод : 4
#######################

# with open('New_Data_Sem\data.txt', 'r', encoding='utf_8') as ls:
#     ls_1 = list(map(str, ls.readline().split()))
#     print(*ls_1)
#     for i in ls_1:
#         if int(i) != ls_1.index(i) + 1:
#             print(int(i) - 1)
#             break


#########################

# Напишите программу Б удоляющюю все слова содержащие  'абв'

#######################

with open('New_Data_Sem\data_2.txt', 'r', encoding='utf_8') as ls:
    li = list(map(str, ls.readline().split()))
    print(li)
    for i in li:
        if 'абв' in i:
            li.remove(i)
    print(li)