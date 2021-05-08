'''
Question 80
Question
Please write a program to print the list after removing
even numbers in [5,6,77,45,22,12,24]
'''

def remove_even(lst):
    new_list = []
    for i in range(len(lst)):
        if  (lst[i] %2):
            new_list.append(lst[i])
    return new_list

a = [5,6,77,45,22,12,24]
# print(remove_even(a))
# print([x for x in a if x%2])

'''
Question 81
Question
By using list comprehension, please write a program to print
the list after removing numbers which are divisible by
5 and 7 in [12,24,35,70,88,120,155].

'''
a = [12,24,35,70,88,120,155]

no_5_7 = [x for x in a if (x%5 ==0) and (x%7 ==0)]
# print(no_5_7)

'''
Question 82
Question
By using list comprehension, please write a program to print
the list after removing the 0th, 2nd, 4th,6th numbers in
[12,24,35,70,88,120,155].
'''

lst = [12,24,35,70,88,120,155]
list_new= [ x for (i,x ) in enumerate(lst) if i % 2!=0 and i <= 6]
# print(list_new)
'''
Question 83
Question
By using list comprehension, please write a program to print
the list after removing the 2nd - 4th numbers in
[12,24,35,70,88,120,155].
'''

a = [12,24,35,70,88,120,155]
a_new = [ x for (i,x) in enumerate (a) if i !=2 or i!=4]
# print(a_new)

'''
Question 84
Question
By using list comprehension, please write a program generate
a 3*5*8 3D array whose each element is 0.
'''

arr = [[[0 for col in range(3)] for col in range(5)] for col in range(8)]
# print(arr)
# print(type(arr))



