from random import randint


print('Игра с конфетами : всего 2021 конфета, 1 ход не более 28 , выигрывает сделавший последний ход')
bank = 28

while bank > 0:
    nam = 28
    if bank < 28 and bank > 0:
        nam = bank
    # player_1 = 1
    player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 1: ваш ход, введите число не более {nam} ->  ')))
    while player == '' or int(player) <= 0 or int(player) > nam:
        player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 1: ваш ход, введите число не более {nam} ->  ')))
    player_1 = int(player)

    bank -= player_1
    print(f'Конфет в Банке осталось -> {bank} !')
    nam = bank
    if bank <= 0:
        print('Выиграл Игрок 1')
        break

    player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 2: ваш ход, введите число не более {nam} ->  ')))
    while player == '' or int(player) <= 0 or int(player) > nam:
        player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 2: ваш ход, введите число не более {nam} ->  ')))
    player_2 = int(player)


    bank -= player_2
    print(f'Конфет в Банке осталось -> {bank} !')
    if bank <= 0:
        print('Выиграл Игрок 2')
        break                          

    bank_1 = bank
    bot = int(randint(1, bank + 1))   
    bank -= bot
    print(f'Игрок Бот, введите число не более {bank_1} -> {bot}')
    print(f'Конфет в Банке осталось -> {bank} !')
    if bank <= 0:
        print('Выиграл Бот')

