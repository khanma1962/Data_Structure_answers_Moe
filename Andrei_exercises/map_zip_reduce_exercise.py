from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def cap(s):
    return s.capitalize()
print('def function output',list(map(cap, my_pets)))

print(list(map(lambda x: x.capitalize(), my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


print(list(zip(my_strings,sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def over_50(num):
    if num > 50: return True

print(list(filter(over_50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
from functools import reduce
def acc(acc, num):
    return acc + num

# all_num = list(zip(my_numbers, scores))
# print(all_num)
# print(reduce(lambda a, b: a+b, my_numbers))
print((reduce(acc, (my_numbers + scores) , 0)))

# print(reduce(acc, my_numbers, 0) )
# print(reduce(acc, scores, 0))

# print(my_numbers + scores)
