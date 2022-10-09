# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sam = 0
# for nam in numbers:
#     sam = sam + nam * nam
# print(sam)





# num = []
# for i in range(int(input())):
#     num.append(int(input()))
# print(*num, sep='\n')
# print()

# for num1 in num:
#     num1 = num1 * num1 + 2 * num1 + 1
#     print(num1)



# l = []
# for i in range(int(input())):
#     i = (int(input()))
#     print(i)
#     l.append(i**2+2*i+1)
# print()
# print(*l, sep='\n')


line = []
for i in range(int(input())):
    i = int(input())
    line.append(i)
line.remove(max(line))
line.remove(min(line))
print(*line, sep='\n')