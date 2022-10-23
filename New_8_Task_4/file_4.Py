# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:- k=2 => 2*x² + 4*x + 5 = 0   k = 6  ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h = 0

#          a, b, c, d, e, h - рандом


from random import randint

for i in range(int(input('Введите натуральную степень многочлена -> ')), 0, -1):
    nam = randint(1, 101)
    if nam == 1:
        nam = ''
    else:
        if i != 1:
            nam = f'{nam}*x**{i} +'
        else:
            nam = f'{nam}*x +'
    print(nam, end=' ')
print(f'{randint(1, 101)} = 0')