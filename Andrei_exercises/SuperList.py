
class SuperList(list):
    def __init__(self, lst):
        self.lst = lst

    def len(self):
        return 1000

    def append(self, num):
        self.lst.append(num)
        return self.lst

    def getitem(self):
        return self.lst.pop()

super_list1 = SuperList([1 ,8 ,9 ,3])
print(super_list1.len())
super_list1.append(5)
print(super_list1.lst)
# print(super_list1.pop())
print(super_list1.getitem())
# print(dir(super_list1))

