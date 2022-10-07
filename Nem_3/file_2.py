# s = 'abcdefghijklmnopqrstuvwxyz'
# print(len(s))
# print()

# s = 'abcABCaswWDE123'
# total = 0
# for i in s:
#     if ord(i) >= 97 and ord(i) <= 122:
#         total += 1
# print(total)

# s = 'aabb AAccDDaa'
# s = s.lower()
# print(s.count(' '))

# s = 'Python'
# total = 0
# for i in s:
#     total += 1
#     if total % 3 == 0:
#        print(i)   


# s = '123@@22@34'
# print(s)

# s = 'a1ffective'
# s1 = s.count('1')
# print(s.count('1') - 2)

# s = 'aective'
# if s.count('f') == 1:
#     print(-1)
# elif s.count('f') == 0:
#     print(- 2)
# else:
#     s = s.replace('f', 'a', 1)
#     print(s.find('f'))
    
s = 'abch12345h'
n1 = s.find('h')
n2 = s.rfind('h')
s_1 = s[n1 + 1:n2]
s_2 = s[n2 - 1:n1:- 1]
s1 = s[:n1 + 1]
s2 = s[n2:]

print(s1)
print(s2)
print(s_2)
print(s_1)
print(s1 + s_2 + s2)
print(s[:n1 + 1] + s[n2 - 1:n1:- 1] + s[n2:])