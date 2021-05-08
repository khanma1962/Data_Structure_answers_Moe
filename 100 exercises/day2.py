'''
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')


'''
def gen_tuple(lst):

    return tuple(lst)

# print('\n', gen_tuple(['34', '67', '55', '33', '12', '98']))

'''
Question 5
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class Question5():
    def __init__(self):
        self.st = ''

    def get_string(self):
        self.st = input('Please input your string :')
    def printString(self):
        return self.st.upper()

q5 = Question5()
# q5.get_string()
# print('\n', q5.printString())

'''
Question 6
Question:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
'''
import numpy as np
def question_6(  D, C=50,H=30):
    val = []
    # items = [x for x in D]
    for i in D:
        val.append(round(np.sqrt((2 * C * i) / H)))
    return ','.join(map(str,val))
# print(question_6(D = [100, 150, 180]))

'''
Question 7
Question:
_Write a program which takes 2 digits, X,Y as input and generates a 
2-dimensional array. The element value in the i-th row and j-th column of 
the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given 
to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
def two_dim_arr(n1, n2):
    lst, lst_2 = [], []

    if n1 == 0 and n2 == 0: # boundary condition
        return []
    for i in range(n1):
        lst = []
        # print(f'i is {i}')
        for j in range(n2):
            # print(f'j is {j}')
            lst.append(i*j)
            # print(f'lst is {lst}')
        lst_2.append(lst)
        # print(f'lst_2 is {lst_2}')
    return lst_2
print(two_dim_arr(3,5))

'''
Question 8
Question:
Write a program that accepts a comma separated sequence of words 
as input and prints the words in a comma-separated sequence after 
sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
'''

def sorted_str(st):
    items = [x for x in st.split(',')]
    # print(f'items is {items}')
    items.sort()
    # print(f'sorted items {items}')
    return ','.join(items)

print(sorted_str('without,hello,bag,world'))

'''
Question 9
Question:
Write a program that accepts sequence of lines as input and prints the 
lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
'''

def cap_words():
    lines = []
    while True:
        s = input('Please input')
        if s:
            lines.append(s.upper())
        else:
            break
    for sentence in lines:
        print(sentence)

# cap_words()


