'''
Question 18
Question:
A website requires the users to input username and password to register. Write a program
to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed,
each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1


'''

def check_email(s):

    words = [x for x in s.split(',')]
    # print(words)
    for word in words:
        d = {'no_lower_case': 0, 'no_upper_case': 0, 'no_num': 0, 'no_sp_char': 0, }

        for char in word:
            if char.isupper():
                d['no_upper_case'] += 1
            elif char.islower():
                d['no_lower_case'] += 1
            elif char.isnumeric():
                d['no_num'] += 1
            else:
                d['no_sp_char'] += 1

        if (len(word) >= 6) and (len(word) <= 12) \
                and d['no_upper_case']\
                and d['no_lower_case'] and d['no_num'] and d['no_sp_char']:
            print(word)


# check_email('ABd1234@1,a F1#,2w3E*,2We3345')

'''
Question 19
Question:
You are required to write a program to sort the (name, age, score) tuples by ascending 
order where name is string, age and score are numbers. The tuples are input by console. 
The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

def sort_name_age():

    lst = []
    while True:
        d = {}
        val = input('Please input name, age, score  :')
        words = [ x for x in val.split(',')]

        if val:
            d['name'] = words[0]
            d['age'] = words[1]
            d['score'] = words[2]
            lst.append(d)
        else:
            break

    for i in lst:
        print(i['age'])

    # print('dict is', d)
    # print('list is ', lst)
    # print(lst[1]['age'])

def sort_name_age2(s):
    # info = input('Please input name, age, score  :')
    info_list = [tuple(x.split(',')) for x in s.split(' ')]
    info_list = sorted(info_list, key = lambda x: (x[0], x[1], x[2]))
    print(info_list)

s = 'Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85'
sort_name_age2(s)

