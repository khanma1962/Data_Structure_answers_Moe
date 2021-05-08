'''
Question 20
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
'''


def seven_multi(start, end):
    for i in range(start, end+1):
        if i % 7 == 0:
            yield i

g = seven_multi(0, 21)
# print(next(g), end = ' ')
# print(next(g), end = ' ')
# print(next(g), end = ' ')
# print(next(g), end = ' ')

'''
Question 21
Question:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, 
DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance 
from current position after a sequence of movement and original point. If the distance 
is a float, then just print the nearest integer. Example: If the following tuples are given 
as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2
'''
import numpy as np
def robot_step():
    x, y = 0, 0
    while True:
        info = input('Please input the movement  : ')
        if not (info):
            break
        info = [x for x in info.split(' ')]
        # print(info)
        if info[0] == 'UP':
            y += int(info[1])
        elif info[0] == 'DOWN':
            y -= int(info[1])
        elif info[0] == 'RIGHT':
            x += int(info[1])
        elif info[0] == 'LEFT':
            x -= int(info[1])

    print(round(np.sqrt(np.square(x) + np.square(y))))


robot_step()



