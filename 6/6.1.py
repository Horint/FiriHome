import random


class CardRank():  # Создаем колоду"

    def __init__(self, deck=None):
        self.deck = list()
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suit = ['♠', '♥', '♣', '♦']
        jocker = ['Red Joker', 'Black Joker']
        #    suit = ['Pi', 'Che', 'Bub', 'Kre', ]
        for x in rank:
            for y in suit:
                self.deck.append(x + y)
        list.append(jocker)
        # list.append['Black Jocker']
        random.shuffle(self.deck)  # сразу её мешаем


koloda_1 = CardRank()  # Создаем экземпляр колоды


class Card():  # создаем класс карта

    def __init__(self):
        self.card = koloda_1.deck.pop(0)  # из колоды достаем карту и удаляем её


class Hand():  # создаем класс рука

    def __init__(self, kolvo, hand=None, ):
        self.kolvo = kolvo  # количесто карт
        self.hand = list()
        for count in list(range(kolvo)):  # немного магии
            x = Card()
            self.hand.append(x.card)

    def show(self):
        return self.hand  ##возвращаем открытые карты хотя можно было бы и через атрибут


print(len(koloda_1.deck))
kolvo = int(input('Сколько карт Вам выдать?: '))
a = Hand(kolvo)
print(a.show())

print(len(koloda_1.deck))

# class Jocker(CardRank):
#     def __init__(self, suit, rank):
#         self.rank = Jocker
#
# class Deck:
#     def __init__(self):
#         self.car