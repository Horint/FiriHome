def dot(sam_pole):
    '''
    :param sam_pole: поле игрока после действия
    :return: Игровое поле, с квадратами
    '''
    dot_pole = []
    for key, val in sam_pole.items():
        dot_pole.append(val)

    dot_pole[:0] = ['а', ' б', 'в', ' г', 'д', 'е', ' ж', ' з', 'и', ' к', ]
    q = 0
    w = 10
    e = 0
    while w <= len(dot_pole):
        print(e, dot_pole[q:w])
        e += 1
        q += 10
        w += 10

class Pole():

    def __init__(self):
        self.x_All = 10

        new_list = []
        riad = list('абвгдежзик')
        stolb = list('12345657890')

        for sam_1 in stolb:
            for sam_2 in riad:
                new = sam_1 + sam_2
                new_list.append(new)

        self.pole = {a: '◻' for a in new_list}
        self.strike_pole = {a: '◻' for a in new_list}

    def add_ship(self, *args):
        try:
            if self.x_All == 0:
                print('Stop')
            else:
                for x in args:
                    if self.pole[x] == '■':
                        print('Поле занято')
                    else:
                        self.pole[x] = '■'
                        self.x_All -= 1
            return dot(self.pole), print(self.x_All)
        except KeyError:
            print('Неправильный порядок ввода \n    Правильно вводить 1а')

    def strike(self, coor, ):
        global end_strike
        if self.pole[coor] == '■':
            self.strike_pole[coor] = '⚑'
            end_strike = False
        else:
            self.strike_pole[coor] = '✘'
            end_strike = True
        return dot(self.strike_pole)



