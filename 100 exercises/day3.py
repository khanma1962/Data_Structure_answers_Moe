'''
Question 10
Question
Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and
sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world

'''

def q10(s):
    # words = set(s.split(' '))
    words = [word for word in s.split(' ')]
    print(words)

    print(' '.join(sorted(list(set(words)))))

# print(q10('hello world and practice makes perfect and hello world again'))

'''
Question 11
Question
Write a program which accepts a sequence of comma separated 4 digit 
binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.
'''

def q11():
    items = []
    while True:
        num = input('Please input number')
        if num:
            if int(num, 2) % 5 == 0 :
                print(num)
                items.append(num)
            else:
                print('Not divisible by 5')
        else:
            break

    return

# print(q11())


'''
Question 12
Question:
Write a program, which will find all such numbers between 1000 and 3000 
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def q12(start, end):
    for i in range(start, end+1):
        if i % 2 == 0:
            print(i, end= ',')
# q12(1000, 3000)

'''
Question 13
Question:
Write a program that accepts a sentence and calculate the number of 
letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
'''

def q13(s):
    is_alpha, is_num = 0, 0
    for i in range(len(s)):
        if s[i].isnumeric():
            is_num += 1
        if s[i].isalpha():
            is_alpha += 1

    print(f'Letters : {is_alpha}')
    print(f'Digits : {is_num}')

def q13_1(s):
    dict = {'is_alpha': 0, 'is_num': 0}
    for i in s:
        if i.isnumeric():
            dict['is_num'] += 1
        if i.isalpha():
            dict['is_alpha'] +=1
    # print(dict)
    print('Letters :', dict['is_alpha'])
    print('Digits :', dict['is_num'])

# q13_1('hello world! 123')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

income = np.random.normal(000, 15000, 10000)
plt.hist(income, 500)
# plt.show()

ar = np.array([[1,2,3,4]])
print(ar.shape)