from model import dot, Pole

a = Pole()
b = Pole()


while a.x_All != 0:
    ship = input('Первый игрок, добавьте корабль:')
    a.add_ship(ship)

while b.x_All !=0:
    ship = input('Второй игрок, добавьте корабль:')
    b.add_ship(ship)

a.x_All = 10
b.x_All = 10

while a.x_All or b.x_All != 0:

    end_strike = False

    while end_strike == False:
        print('Ход первого игрока')
        strike = input('Введите координаты: ')
        b.strike(strike)
        b.x_All -= 1
        if b.shot == True:
            end_strike = False
        else:
            end_strike = True

        print(end_strike)

    end_strike = False

    while end_strike == False:
        print('Ход второго игрока')
        strike = input('Введите координаты: ')
        a.strike(strike)
        a.x_All -= 1
        if a.shot == True:
            end_strike = False
        else:
            end_strike = True

print('Конец')

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print()
#         print('Shutting down, bye!')