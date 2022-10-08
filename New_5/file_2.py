# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат. Примечание:  Используйте знания об Алгебра Логике,
# вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1)


x, y, z, = 0, 0, 0
if not (x + y + z) == (not x) * (not y ) * (not z):
    x, y, z = 1, 0, 0
    if not (x + y + z) == (not x) * (not y ) * (not z):
        x, y, z = 0, 1, 0
        if not (x + y + z) == (not x) * (not y ) * (not z):
            x, y, z = 0, 0, 1
            if not (x + y + z) == (not x) * (not y ) * (not z):
                x, y, z = 1, 1, 0
                if not (x + y + z) == (not x) * (not y ) * (not z):
                    x, y, z = 1, 0, 1
                    if not (x + y + z) == (not x) * (not y ) * (not z):
                        print('True')
else:
    print('False')