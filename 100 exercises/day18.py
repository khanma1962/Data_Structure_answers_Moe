
"""
Question 70
Question
Please write a program to output a random even number between
0 and 10 inclusive using random module and list comprehension.
"""
import random
# print(random.choice([x for x in range(11) if x%2 == 0]))
'''
Question 71
Question
Please write a program to output a random number, which is
divisible by 5 and 7, between 10 and 150 inclusive using
random module and list comprehension.

Hints
Use random.choice() to a random element from a list.
'''
import random
# print(random.choice([x for x in range(10, 151) if (x%5==0) and (x%7==0)]))

'''
Question 72
Question
Please write a program to generate a list with 5 random numbers
between 100 and 200 inclusive.

Hints
Use random.sample() to generate a list of random values.
'''
import random
# print(random.sample(range(100,201), 5))

'''
Question 73
Question
Please write a program to randomly generate a list with 5
even numbers between 100 and 200 inclusive.
'''
import random
# print(random.sample([x for x in range(100,200) if not (x%2)], 5))

'''
Question 74
Question
Please write a program to randomly generate a list with 5 numbers,
which are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''
import random
print(random.sample([ x for x in range(0, 1000) if (x%5 ==0) and (x%7 ==0)], 5))




