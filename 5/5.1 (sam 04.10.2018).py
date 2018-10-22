class Korzina():

    def __init__(self, size, ostatok = None):
        self.size= int(size)
        if ostatok is None:
            ostatok = int()
        self.ostatok = ostatok
        
    
    def put_in(self, obj):
        if self.ostatok == 0:
            self.ostatok = self.size - obj.size
            if self.ostatok <= 0:
                print('Mesta bolshe neet')
        else:
            self.ostatok -= obj.size
            if self.ostatok <= 0:
                print('Mesta bolshe neet')
            return self.ostatok     
            
            
kor = Korzina(10)
              

class Food():
    def __init__(self, size, name):
        self.name = name
        self.size = size

egg = Food(2, 'egg')
meat = Food(5, 'meat')
apple = Food(9, 'apple')
print(kor.put_in(egg))
