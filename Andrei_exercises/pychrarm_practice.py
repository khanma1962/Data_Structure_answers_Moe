

class PlayerCharacter():
    membership = True
    def __init__(self, name, age):
        if self.membership:
            self._name = name
            self._age = age

    def shout(self):
        print(f'my name is {self._name}')
        return 'done'

    @classmethod
    def adding_thing(cls, n1, n2):
        return n1 + n2

    @staticmethod
    def adding_thing2(n1, n2):
        return n1 + n2


player1 = PlayerCharacter('Moe', 58)
# print(player1.name)
# print(player1.age)
# print(player1.shout())
# print(PlayerCharacter.adding_thing2(5,4))
# player1.attack = 50
# print(f'player1 attack is {player1.attack}')
# player1.name = 'no_name'
# player1.shout = 'BOOOO'
print(player1._name)
print(player1.shout())
# print(player1.name())