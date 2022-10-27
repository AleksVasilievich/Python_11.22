# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# *** b) Подумайте как наделить бота ""интеллектом"" (Теория игр)


from random import randint


print('Игра с конфетами : всего 2021 конфета, 1 ход не более 28 , выигрывает сделавший последний ход')
bank = 202

while bank > 0:
    nam = 28
    if bank < 28 and bank > 0:
        nam = bank
    # player_1 = 1
    player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 1: ваш ход, введите число не более {nam} ->  ')))
    while player == '' or int(player) <= 0 or int(player) > nam:
        player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 1: ваш ход, введите число не более {nam} ->  ')))
    player_1 = int(player)
    
    # while player_1 <= 0 or player_1 > nam:
    #         player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 1: ваш ход, введите число не более {nam} ->  ')))
    # while player == '':
    #     player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 1: ваш ход, введите число не более {nam} ->  ')))
    # player_1 = int(player)

        # player_1 = input(f'Игрок 1: ваш ход, введите число не более {nam} ->  ')
    
    bank -= player_1
    print(f'Конфет в Банке осталось -> {bank} !')
    nam = bank
    if bank <= 0:
        print('Выиграл Игрок 1')
        break
    
    nam = 28
    if bank < 28 and bank > 0:
        nam = bank
    
        # player_1 = 1
    player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 2: ваш ход, введите число не более {nam} ->  ')))
    while player == '' or int(player) <= 0 or int(player) > nam:
        player = ''.join(filter(lambda x: x.isdigit(), input(f'Игрок 2: ваш ход, введите число не более {nam} ->  ')))
    player_2 = int(player)

    # player_2 = int(input(f'Игрок 2: ваш ход, введите число не более {nam} ->  '))
    # while player_2 <= 0 or player_1 > nam:
    #     player_2 = int(input(f'Игрок 2: ваш ход, введите число не более {nam} ->  '))

    bank -= player_2
    print(f'Конфет в Банке осталось -> {bank} !')
    nam = bank
    if bank <= 0:
        print('Выиграл Игрок 2')
        break                           # нужен если участвует следующий игрок.

    # bank_1 = bank
    # bot = int(randint(1, bank + 1))   
    # bank -= bot
    # print(f'Игрок Бот, введите число не более {bank_1} -> {bot}')
    # print(f'Конфет в Банке осталось -> {bank} !')
    # if bank <= 0:
    #     print('Выиграл Бот')
