
from functools import reduce
my_list = [4, 7, 1, 99]

print(list(map(lambda items : items *2, my_list)))

print(list(filter(lambda items: items % 2, my_list)))

print(reduce(lambda  acc, items: acc + items, my_list))

#square
print(list(map(lambda x: x*x, my_list)))

# sort list
a = [(3, 4), (9, 1), (2, 8), (10, -1)]
# print(sorted(a, key=lambda x:  x[1]))
a.sort(key = lambda x: x[1])
print(a)

import pandas as pd
import numpy as np
z = np.array([6,7,8])
