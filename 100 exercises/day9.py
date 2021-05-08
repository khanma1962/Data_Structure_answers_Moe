'''
Question 26
Question:
Define a function which can compute the sum of two numbers.

'''
def compute_sum(n1, n2):
    return n1 + n2
# print(compute_sum(5,6))

'''
Question 27
Question:
Define a function that can convert a integer into a string and print it in console.
'''
def conv_int(n1):
    char = str(n1)
    for i in char:
        print(i, end = ' ')
# conv_int(8998765)


'''
Question 28
Question:
Define a function that can receive two integer numbers in string form and compute 
their sum and then print it in console.
'''
def compute_sum(s1, s2):
    n1 , n2 = int(s1), int(s2)
    return n1 + n2
# print(compute_sum('876', '65'))

'''
Question 29
Question:
Define a function that can accept two strings as input and concatenate them and then 
print it in console.
'''
import numpy as np
def con_string(s1, s2):
    print(s1 + s2)
    print(''.join([s1, s2]))

# con_string('ewr', 'sfg')

'''
Question 30
Question:
Define a function that can accept two strings as input and print the string with 
maximum length in console. If two strings have the same length, then the function 
should print all strings line by line.

'''
def string_len(s1, s2):
    s1_len, s2_len = len(s1), len(s2)
    if s1_len > s2_len:
        print(s1)
    elif s1_len < s2_len:
        print(s2)
    else:
        print(s1)
        print(s2)

string_len('fwer', 'fwer')

