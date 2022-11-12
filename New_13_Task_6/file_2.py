# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#  [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

ls = [12,'sadf',5643]
print(list(filter(lambda i: type(i) == str, ls)), list(filter(lambda i: type(i) != str, ls)))

# def filters(ls):
#     res_str = []
#     res_float = []
#     ls = [12,'sadf',5643]
#     for i in ls:
#         if type(i) == str:
#             res_str.append(i)
#         else:
#             res_float.append(i)
#     return res_str, res_float

# lst = [12,'sadf',5643]
# print(filters(lst))