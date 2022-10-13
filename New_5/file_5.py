# s = 'У лукоморья дуб зеленый златая цепь на дубе том'
# print(*input().split(), sep='\n')
#------------------------------------

# s ='Владимир Семенович Высоцкий' 
# sl = s.split()
# print(*[i[0] for i in s.split()], sep='.')


n = '12345'; s = '+' 
n = ','.join(n); n = n.split(',')
for i in range(len(n)):
    n[i] = int(n[i])
    for j in range(n[i]):
        print(s)
print()