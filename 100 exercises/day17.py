'''
Question 65
Question
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
'''

def assert_list(lst):
    for i in lst:
        # print(i)
        assert i % 2 == 0
# assert_list([2, 4, 6, 7, 8])


"""
Question 66
Question
Please write a program which accepts basic mathematic expression from console and print 
the evaluation result.

Example: If the following n is given as input to the program:
35 + 3
Then, the output of the program should be:

38
"""
def math_cal():
    info = input('Please input the equation  : ')
    words = info.split('+')
    print(int(words[0] )+ int(words[1]))

# math_cal()

# info = input("please enter equation  :")
# print(eval(info))
'''
Question 67
Question
Please write a binary search function which searches an item in a sorted list. The function should 
return the index of element to be searched in the list.
'''
def bin_search(lst, num):
    left, right = 0, len(lst)-1
    while left <= right:
        mid = round((left + right) /2)
        # print('left, right, mid', left, right, mid)
        if lst[mid] == num:
            # print(' equal', lst[mid])
            print(f'Number {num} is at {mid}')
        if lst[mid] > num:
            # print(' > ', lst[mid])
            right = mid  - 1
        else:
            left = mid + 1

a = [2,3, 4, 5, 6, 7, 8, 9]
# bin_search(a, 5)

'''
Question 68
Question
Please generate a random float where the value is between 10 and 100 
using Python module.
'''
# import numpy as np
import random

# print(float(random.uniform(10,100)))

'''

Question 69
Question
Please generate a random float where the value is between 5 and 95 
using Python module.
'''
# print(random.uniform(5 , 95))




