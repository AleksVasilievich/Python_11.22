# num = int(input('Введите число от 1 до 7 -> '))

# if num == 6 or num == 7:
#     print('День является выходным')
# elif num == 1 or num == 2 or num == 3 or num == 4 or num == 5:
#     print('День не является выходым')
# else:
#     print('Введите число от 1 до 7')

# n = 113222
# s = 0
# while n % 10 > 0:
#     if (n % 10) / 2 == 0:
#         s += n % 10
#     n = n // 10
#     print(s)


# n = 234
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n = n // 10 
# print(s)


# n = 4
# count = 0
# maximum = 0
# for i in range(n):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = 7
# print('*******************')
# for i in range(n - 2):
#     print('*                 *')
# print('*******************')

# n = 134
# if n > 1000:
#     n = n // 10
# n = n % 10
# print(n)

# n = 255
# count_3 = 0; final = 0; final_s = 0 
# count_2 = 0; sam_5 = 0; mult_7 = 1; sam_0_5 = 0

# final = n % 10
# while n != 0:
#     if n % 10 == 3:
#         count_3 += 1

#     if n % 10 == final:
#         final_s += 1
    
#     if n % 2 == 0:
#         count_2 += 1

#     if n % 10 > 5:
#         sam_5 += n % 10

#     if n % 10 > 7:
#         mult_7 *= n % 10
#     else:
#         mult_7 == 1

#     if n % 10 == 0 or n % 10 == 5:
#         sam_0_5 += 1
#     n = n // 10

# print(count_3)    
# print(final_s)
# print(count_2)
# print(sam_5)
# print(mult_7)
# print(sam_0_5)   


# n = 1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683,
#    1729 = 1**3 + 12**3 = 9**3 + 10**3

# a, b, c, d = 1, 12, 9, 10

# for a in range(1, 50):
#     for b in range(1, 50):
#         for c in range(1, 50):
#             for d in range(1, 50):
#                 if a != b and a != c and a != d and b != c and b != d and c != d and a ** 3 + b ** 3 == c ** 3 + d ** 3:
#                     print(a ** 3 + b ** 3)




# for hours in range(24):
#     for minutes in range(60):          # электронные часы !
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)


# s = '12345'
# for c in s:
#     print(c)

# n = 'Hi 1Python'
# s = 'Цифр нет'
# for i in range(len(n)):
#     if n[i] in '0123456789':
#         s = 'Цифра'
# print(s)


# print('Цифра' if set('1234567890') & set(input()) else 'Цифр нет')  
#         #  & это и  побитово!


# s = input()
# if len(s) == 1 and s in 'asdf':
#     print('YES')



# s = 'Вдохновение – это умение приводить себя в рабочее состояние!'
# vowels = 'ауоыиэяюёе'
# vowels_num = 0
# consonants = 'бвгджзйклмнпрстфхцчшщ'
# consonants_num = 0
# for i in s.lower():
#     if i in vowels:
#         vowels_num += 1
#     if i in consonants:
#         consonants_num += 1
# print('Количество гласных букв равно', vowels_num)
# print('Количество сгласных букв равно', consonants_num)


# n = int(input())
# n_to = ''
# while n != 0:
#     if n - (n // 2) * 2 == 1:
#         n_to += '1'                    #  десятичное в двоичное!
#         n = n // 2
#     elif n - (n // 2) * 2 == 0:
#         n_to += '0'
#         n = n // 2
# for i in range(len(n_to) - 1, -1, -1):
#     print(n_to[i], end='')


# s = 'potop' 
# s_n = s[::-1]
# if s[:len(s) // 2 + 1] == s_n[:len(s) // 2 + 1]:      # полиндром или нет!
#     print('YES')
# else:
#     print('NO')