# Пользователь вводит число, Вам необходимо вывести число Пи 
# с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

# Применим  формулу Бэйли — Боруэйна — Плаффа 

n = 1000
pi = 0
for x in range(n):
    pi = pi + (1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)))
print(pi)
print(round(pi, 2))


