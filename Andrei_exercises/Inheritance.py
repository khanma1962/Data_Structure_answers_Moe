class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do nothing')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with the {self.num_arrows} arrows ')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__( email)
        # User.__init__(self, email) # this is another way to call user
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with the power of {self.power}')


wizard1 = Wizard('bill', 45, 'sd@asdf.com')
archer1 = Archer('andy', 90)
# print(wizard1.email)

# def player_attack(char):
#     char.attack()

# player_attack(wizard1)
# player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()
print(dir(wizard1))