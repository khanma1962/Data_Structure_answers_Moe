'''
Question 95
Question
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given scores.
Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5
2 3 6 6 5
Then, the output of the program should be:

5
'''

a = [2 ,3 ,6 ,6 ,5]
b =  list(set(sorted(a)))
# print(b[-2])
'''
Question 96
Question
You are given a string S and width W. Your task is to wrap the 
string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
import textwrap

s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
num =4
ans = textwrap.wrap(s, 4)
# for i in ans:
#     print(i)

'''
Question 97
Question
You are given an integer, N. Your task is to print an alphabet rangoli 
of size N. (Rangoli is a form of Indian folk art based on creation of 
patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

















'''
Question 98
Question
You are given a date. Your task is to find what the day is on that date.

Input

A single line of input containing the space separated month, day and 
year, respectively, in MM DD YYYY format.

08 05 2015
Output

Output the correct day in capital letters.

WEDNESDAY
'''
# import calendar
# # info = input('Please input the dates  :')
# mm, day, yr = map(int, info.split())
#
# day_id = calendar.weekday(yr,mm,day)
# # print(calendar.day_name[day_id].upper())

'''
Question 99
Question
Given 2 sets of integers, M and N, print their symmetric 
difference in ascending order. The term symmetric difference 

indicates those values that exist in either M or N but do not exist 
in both.

Input

The first line of input contains an integer, M.The second line 
contains M space-separated integers.The third line contains an 
integer, N.The fourth line contains N space-separated integers.

4
2 4 5 9
4
2 4 11 12
Output

Output the symmetric difference integers in ascending order, 
one per line.

5
9
11
12
'''
m = input("M input :")
m = set(map(int, m.split()))

n = input("N input :")
n = set(map(int, n.split()))

print( n ^ m)

