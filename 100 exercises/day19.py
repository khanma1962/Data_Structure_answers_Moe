''':
Question 75
Question
Please write a program to randomly print a integer number
between 7 and 15 inclusive.
'''

import random
# print(random.randint(7,15))
# print(random.randrange(7,15))

'''
Question 76
Question
Please write a program to compress and decompress the string
"hello world!hello world!hello world!hello world!".
'''
import zlib
s = "hello world!hello world!hello world!hello world!"
y = bytes(s, 'utf-8')
t = zlib.compress(y)
# print(t)
#
# print(zlib.decompress(t))

'''
Question 77
Question
Please write a program to print the running time of execution
of "1+1" for 100 times.
'''
import datetime
def pr(x, y, num):
    before = datetime.datetime.now()
    for i in range(num):
        z = x+y
    after = datetime.datetime.now()
    return after - before

# print(pr(2,3, 10**8))

'''

Question 78
Question
Please write a program to shuffle and print the list [3,6,7,8].
'''

import random
a =  [3,6,7,8]
random.shuffle(a)
# print(a)

'''
Question 79
Question
Please write a program to generate all sentences where
subject is in ["I", "You"] and verb is in ["Play", "Love"] and
the object is in ["Hockey","Football"].
'''

subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey","Football"]

for x in subject:
    for y in verb:
        for z in object:
            sentence = x, y, z
            # print(sentence)




