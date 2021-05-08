'''
Question 100
Question
You are given words. Some words may repeat. For each word,
output its number of occurrences. The output order should
correspond with the input order of appearance of the word.
See the sample input/output for clarification.

If the following string is given as input to the program:

4
bcdef
abcdefg
bcde
bcdef
Then, the output of the program should be:

3
2 1 1

'''


def check_dict():
    word_list = []
    word_dict = {}
    info = int(input('Pleaes input the no. of strings  :'))
    for i in range(info):
        s = input('Please input string  :')
        if s not in word_list:
            word_list.append(s)
        word_dict[s] = word_dict.get(s, 0) + 1

    for k,v in word_dict.items():
        print(v)

# check_dict()

'''
Question 101
Question
You are given a string.Your task is to count the frequency of letters of
 the string and print the letters in descending order of frequency.

If the following string is given as input to the program:

aabbbccde
Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1
'''
def count_freq(s):
    dict = {}
    for char in s:
        dict[char] = dict.get(char, 0) + 1

    d = sorted(dict.items(), key= lambda x: -x[1])

    for i in d:
        print(i[0], i[1])

# count_freq('aabbbccde')

'''
Question 102
Question
Write a Python program that accepts a string and calculate the 
number of digits and letters.

Input

Hello321Bye360
Output

Digit - 6
Letter - 8
'''
def string_check(s):
    dig, let = 0, 0
    for char in s:
        # print('char is', char)
        if char.isalpha():
            # print('check if alpha', char.isalpha())
            dig += 1
        elif char.isdigit():
            let += 1
    print(f"No. of digits are {dig} and no. of letters are {let}")

string_check('Hello321Bye360')

