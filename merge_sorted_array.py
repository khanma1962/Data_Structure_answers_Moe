# Spder environment
arr1 = [1, 2, 5, 7, 9]
arr2 = [3,4,6,8,11]
# print('Array at 2',arr1[2])
# def merge_sorted_array(a, b):
#     x = a + b
#     # print('x is ', x)
#     x.sort()
#     return x
# print('The merged array is ',merge_sorted_array(arr1, arr2))
def merge_sorted_array2(a, b):
    if len(a) < 1 and len(b) < 1: # boundary condition
        return a+b   
    i, j = 0, 0
    sorted_list = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        elif b[j] < a[i]:
            sorted_list.append(b[j])
            j += 1
        # print('sorted_list  is', sorted_list)   
    return sorted_list+ a[i:] + b[j:]

print('The merged array is ',merge_sorted_array2(arr1, arr2))






