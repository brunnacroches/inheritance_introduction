class Mother:
    
    def __init__(self, address) -> None:
        self.address = address
        self.last_name = 'Stuart'
    
    def eat(self) -> None:
        print('I am eating!')
    
    def study(self) -> None:
        print('I am studing')

class Daughter(Mother):
    
    def __init__(self, address) -> None:
        super().__init__(address)
    
    def play(self, toy: str) -> None:
        print('I am playing with {}'.format(toy))

class Granddaughter(Daughter):
    
    def __init__(self, address) -> None:
        super().__init__(address)

maria = Mother('Streat Balon')
susan = Daughter('Streat Circle')
susan.play('doll')

print(maria.address)
print(susan.address)