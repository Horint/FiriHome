def dot(sam_pole):
    '''
    :param sam_pole: поле игрока после действия
    :return: Игровое поле, с квадратами
    '''
    dot_pole = []
    for key, val in sam_pole.items():
        if val is True:
            dot_pole.append('■')
        else:
            dot_pole.append('◻')

    dot_pole[:0] = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', ' з', ' и', ' к', ]
    q = 0
    w = 10
    e = 0
    dot_pole
    while w <= len(dot_pole):
        print(e, dot_pole[q:w])
        e += 1
        q += 10
        w += 10

    return print('Осталось раставить кораблей: ')


class Pole():

    def __init__(self):
        self.x_4 = 1
        self.x_3 = 2
        self.x_2 = 3
        self.x_1 = 4

        new_list = []
        riad = list('абвгдежзик')
        stolb = list('12345657890')

        for sam_1 in stolb:
            for sam_2 in riad:
                new = sam_1 + sam_2
                new_list.append(new)

        self.pole = {a: False for a in new_list}

    def add_ship_x1(self, coor, ):
        if self.x_1 == 0:
            print('Stop')
        else:
            if self.pole[coor] is True:
                print('a', 'Поле занято')
            else:
                self.pole[coor] = True
                self.x_1 -= 1

        return dot(self.pole), self.x_1

    def add_ship_x2(self, coor_1, coor_2):
        if self.x_2 == 0:
            print('Stop')
        else:
            if self.pole[coor_1] is True:
                print('Поле занято')
            elif self.pole[coor_2] is True:
                print('Поле занято')
            else:
                self.pole[coor_1] = True
                self.pole[coor_2] = True
                self.x_2 -= 1

        return dot(self.pole)

    def add_ship_x3(self, coor_1, coor_2, coor_3):
        if self.x_3 == 0:
            print('Stop')
        else:
            if self.pole[coor_1] is True:
                print('Поле занято')
            elif self.pole[coor_2] is True:
                print('Поле занято')
            elif self.pole[coor_3] is True:
                print('Поле занято')

            else:
                self.pole[coor_1] = True
                self.pole[coor_2] = True
                self.pole[coor_3] = True
                self.x_3 -= 1

        return dot(self.pole)

    def add_ship_x4(self, coor_1, coor_2, coor_3, coor_4):
        if self.x_4 == 0:
            print('Stop')
        else:
            if self.pole[coor_1] is True:
                print('Поле занято')
            elif self.pole[coor_2] is True:
                print('Поле занято')
            elif self.pole[coor_3] is True:
                print('Поле занято')
            elif self.pole[coor_4] is True:
                print('Поле занято')

            else:
                self.pole[coor_1] = True
                self.pole[coor_2] = True
                self.pole[coor_3] = True
                self.pole[coor_4] = True
                self.x_4 -= 1

        return dot(self.pole)


a = Pole()
##print(a.add_ship_x2('1а', '2а'))




