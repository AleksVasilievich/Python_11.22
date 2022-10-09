# n = 5
# # num = [i for i in range(n)]
# print(list(range(1, n + 1)))

# n = 5
# ls1 = []
# ls = list(range(97, 97 + n))
# for i in ls:
#     ls1 += chr(i)
# print(ls1)

# ls = list(chr(i) for i in range(97, 97 + n))
# print(ls)

# numbers = [2, 4, 6, 8, 10]
# print(numbers[1:3])
# print(numbers[2:5])

# fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
# fruits[2:5] = ['банан', 'вишня', 'киви']

# print(fruits)

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = 0
# for i in evens:
#     average += i
# average = average / len(evens)

# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[-1] = 'Фиолетовый'
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[-1::-1])

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]

# print(numbers1 * 2 + numbers2 * 9 + numbers3)

words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']
s = '12'
# words1.append('python')
# words2.extend('python')
words1.append(s)
words2.extend(s)

print(words1)
print(words2)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# print(len(numbers))
# print(numbers[-1])
# print(numbers[-1::-1])

# if 17 and 5 in numbers:
#     print('YES')
# else:
#     print('NO')
    
# del numbers[-1]
# del numbers[0]

# print(numbers)