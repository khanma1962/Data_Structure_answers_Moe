'''
Question 44
Question:
Write a program which can map() to make a list whose elements are square of numbers
between 1 and 20 (both included).
'''

def sq(n):
    return n ** 2

res = list(map(sq,[x for x in range(1, 21)]))
# print(res)

sq_num = list(map(lambda x: x**2, range(1,21)))
# print(sq_num)

'''
Question 45
Question:
Define a class named American which has a static method called printNationality.
'''

class American(object):
    # def __init__(self):

    @staticmethod
    def printNationality():
        print('American')

a = American()
# a.printNationality()

'''
Question 46
Question:
Define a class named American and its subclass NewYorker.
'''

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)




