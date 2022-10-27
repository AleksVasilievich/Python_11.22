# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
################################################################################

# stroka = ''.join(input().split())
stroka = 'faaabbbbgccbbba'
stroka_z = []
count = 1
n = 1

for i in stroka[: -1]:
    j = stroka[n]
    if i == j:
        count += 1
        n += 1
    else:
        if count == 1:
            stroka_z.append(i)
            n += 1
            count = 1
        else:
            stroka_z.append(str(count))
            stroka_z.append(i)
            n += 1
            count = 1
if i != j:
    stroka_z.append(stroka[-1])
    
print(''.join(stroka_z))
