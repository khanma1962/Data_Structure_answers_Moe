# list , set, dictionary comprehension
#list
def add_list(s):
    my_list = []
    for char in s:
        my_list.append(char)
    return my_list

# print("".join(add_list('hello')))

my_list = []
# my_list1 = [x for x in 'hello']
# my_list2 = [x for x in range(100)]
# my_list3 = [2*x for x in range(100)]
def only_odd(var):
    print(var % 2)
    return var % 2 != 0
# my_list4 = list(filter(only_odd, [x**2 for x in range(100)]))
my_list5 = [x**2 for x in range(100) if x**2 % 2 != 0 ]
print(my_list5)


#set

my_list6 = {x for x in 'hello'}
my_list7 = {x for x in range(100)}
print(my_list7)


#dictionary comprehension

simple_dict = {
    'address' : 20,
    'age' : 35
}

my_dict = {k:v**2 for k, v in simple_dict.items() if v%2 == 0}
my_dict2 = {num:num*2 for num in [1, 5, 9, 12]}
print(my_dict2)
print(my_dict2[5])



# finding duplicates
some_list = [90, 1, 60, 4, 90, 23, 4, 56, 60]

def finding_dup(arr):
    dup = []
    if len(arr) <= 1:
        return arr
    for val in arr:
        if val not in dup:
            dup.append(val)
    return dup

# print(finding_dup(some_list))

duplicates =  {x for x in some_list}
# duplicates = some_list - duplicates
duplicates2 =set ([ x for x in some_list if some_list.count(x)  > 1])
print(duplicates)
