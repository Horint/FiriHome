# import random
#
# class CardRank(): # Создаем колоду"
#
#     def __init__ (self, deck = None):
#         self.deck = list()
#         rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
#         suit = ['Pi', 'Che', 'Bub', 'Kre', ]
#         for x in rank:
#             for y in suit:
#                 self.deck.append(x+y)
#         random.shuffle(self.deck) # сразу её мешаем
#
# koloda_1 = CardRank()                             # Создаем экземпляр колоды
#
# class Card(): #создаем класс карта
#
#     def __init__(self):
#         self.card = koloda_1.deck.pop(0)       #из колоды достаем карту и удаляем её
#
# class Hand():                                              #создаем класс рука
#
#     def __init__ (self,kolvo = 3, hand = None,):
#         self.kolvo = kolvo
#         self.hand = list()
#         for count in list(range(kolvo)):    # немного магии
#             x = Card()
#             self.hand.append(x.card)
#
#     def show(self):
#         return self.hand                         ##возвращаем открытые карты хотя можно было бы и через
# while True:
#     first_bank = 100
#     second_bank = 100
#     first_stavka = int(input('Ставка первого игрока: '))
#     first_bank -= first_stavka
#     second_stavka = int(input('Ставка второго игрока: '))
#     second_bank -= second_stavka
#     first_hand = Hand(3)
#     print('Первый игрок',first_hand.show())
#     second_hand = Hand(3)
#     print("Второй игрок",second_hand.show())
#
#     first = input('Первый игрок: Фолд | Чек | Рей: ')
#     first = first.lower()
#     if first == 'фолд':
#         second_bank += first_stavka + second_stavka
#         print('Банк первого игрока', first_bank)
#         print('Банк второго игрока', second_bank)
#         print('the end')
#     elif first == 'чек':
#         pass
#     elif first == 'рей':
#         first_stavka += int(input('Ставка первого игрока: '))
#         print(first_stavka)
#
#     second = input('Второй игрок: Фолд | Чек | Рей: ')
#     second = second.lower()
#     if second == 'фолд':
#         first_bank += first_stavka + second_stavka
#         print('Банк первого игрока', first_bank)
#         print('Банк второго игрока', second_bank)
#         print('the end')
#     elif second == 'чек':
#         pass
#     elif second == 'рей':
#         second_stavka += int(input('Ставка второго игрока: '))
#         print(second_stavka)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
