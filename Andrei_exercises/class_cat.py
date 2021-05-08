class Cat():
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Al', 5)
cat2 = Cat('Bill', 6)
cat3 = Cat('Cindy', 9)


def get_oldest(*args):
    return max(args)


# to find the name of the oldest cat
old = get_oldest(cat1.age, cat2.age, cat3.age)
print(f'The oldest cat is {old} years old')
