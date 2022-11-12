print(list(map(lambda x: x**3, (i for i in range(1, 11) if i % 2 == 0))))

print(list((i, i**3) for i in range(1, 11) if i % 2 == 0))
