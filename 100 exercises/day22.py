'''
Question 90
Question
Please write a program which count and print the numbers of
each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

def count_char(s):
    d = {}
    for i in s:
        d[i] = d.get(i,  0) +1
        # print('d is ',s[i], d)
    return d
a = 'abcdefgabc'
b = count_char(a)
# for k,v in b.items():
    # print(k,v)

'''
Question 91
Question
Please write a program which accepts a string from console and 
print it in reverse order.

Example: If the following string is given as input to the program:*

rise to vote sir
Then, the output of the program should be:

ris etov ot esir
'''
def rev_string2(s):
    words = s.split()
    # print('words ', words)
    for word in words[::-1]:
        for i in range(len(word)):
            print(word[len(word)-1 - i], end = ' ')
        print('', end = '   ')

def rev_string(s):
    words = s.split()
    words_rev = []
    for i in range(len(words)):
        words_rev.append(words[len(words) -1 - i])
    # print(words_rev)
    for word in words_rev:
        for i in range(len(word)):
            print(word[len(word)-1 - i], end = ' ')
        print('', end = '   ')


s = 'rise to vote sir'
# rev_string(s)

'''
Question 92
Question
Please write a program which accepts a string from console and 
print the characters that have even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:

Helloworld
'''
def print_char(s):
    output = []
    for char in s:
        if char.isalpha():
            output.append(char)
    print("".join(output))

s = 'H1e2l3l4o5w6o7r8l9d'
# print_char(s)

'''
Question 93
Question
Please write a program which prints all permutations of [1,2,3]
'''
import itertools
a = [1, 2, 3]
# print(list(itertools.permutations(a, 2)))

'''
Question 94
Question
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits
 in a farm. How many rabbits and how many chickens do we have?
'''
rabbits, chickens = 35, 0

while rabbits >= 0:
    if (4* rabbits + 2*chickens) == 94:
        print(f' There are {rabbits} rabbits and {chickens} chickens')
        break
    else:
        rabbits -= 1
        chickens += 1





