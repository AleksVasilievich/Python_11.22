# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#  [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

ls = list(filter(lambda i, type(i)= str))