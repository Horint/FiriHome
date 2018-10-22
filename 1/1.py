mos_dict = { 'Что такое Москва?' : 'Река''Город' 'река'
                }
sun_dict = {'Что яркое светит на небе днем?' : "Солнце" 'Звезда'
                }
blood_dict = {'Что для Кровавого Бога?' :'Кровь для Кровавового Бога''Черепа для Трона Черепов'
              'КРОВЬ'
        }

print('Что такое Москва?')

answer_1 = input()
while answer_1 not in mos_dict['Что такое Москва?']:
    print('Нет')
    print ('Что такое Москва?')
    answer_1 = input()
else:
    print('Да')
    print('Что яркое светит на небе днем?')
    answer_2 = input()

while answer_2 not in sun_dict['Что яркое светит на небе днем?']:
    print('Нет')
    print ('Что яркое светит на небе днем?')
    answer_2 = input()
else:
    print ('Да')
    print ('Что для Кровавого Бога?')
    answer_3 = input()
    
while answer_3 not in blood_dict['Что для Кровавого Бога?']:
    print('Нет')
    print ('ЧТО ДЛЯ КРОВАВОГО БОГА???')
    answer_3 = input()
else:
    print ('Да')

print ('Молодец!')
            