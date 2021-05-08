'''
Question 85
Question
By using list comprehension, please write a program to print the
list after removing the 0th,4th,5th numbers in
[12,24,35,70,88,120,155].
'''

lst = [12,24,35,70,88,120,155]
lst_new = [ x for (i,x) in enumerate(lst) if not(i==0 or i ==4 or i==5)]
# print(lst_new)
'''

Question 86
Question
By using list comprehension, please write a program to print 
the list after removing the value 24 in [12,24,35,24,88,120,155].
'''
a = [12,24,35,24,88,120,155]
a_new = [ x for x in a if x != 24]
# print(a_new)

'''
Question 87
Question
With two given lists [1,3,6,78,35,55] and 
[12,24,35,24,88,120,155], write a program to make a 
list whose elements are intersection of the above given lists.
'''
def intersection_of_2_list(lst1, lst2):
    # print('lst1 is ', lst1)
    lst_new = []
    for i in range(len(lst1)):
        # print('i is ',lst1[i])
        if lst1[i] in lst2:
            lst_new.append(lst1[i])
    return lst_new

a = [1,3,6,78,35,55]
b = [12,24,35,24,88,120,155]
# print(intersection_of_2_list(a,b))
a_union_b = [ x for x in a if x in b]
# print(a_union_b)

'''
Question 88
Question
With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all 
duplicate values with original order reserved.
'''
def remove_dup(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst

a = [12,24,35,24,88,120,155,88,120,155]
# print(remove_dup(a))
'''

Question 89
Question
Define a class Person and its two child classes: 
Male and Female.
 All classes have a method "getGender" which can print
  "Male" for Male class and "Female" for Female class.
'''
class Person(object):
    def __init__(self):
        self.gender = 'Unknown'
    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self):
        self.gender = 'Male'

class Female(Person):
    def __init__(self):
        self.gender = 'Female'


m = Male()
f = Female()
print(m.getGender())
print(f.getGender())

