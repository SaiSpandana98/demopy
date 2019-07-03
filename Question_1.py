def binary_search(list1, l, r, x):

     while l<=r:
        mid = (l + r)//2
        if list1[mid] == x:
            return mid
        elif list1[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
     return -1

list1 = [2, 4, 12, 7, 9, 29]

x = int(input('Énter a number to be searched in the list'))
result = binary_search(list1, 0, len(list1)-1, x )
if result != -1:
    print('Element is found at index %d'%result)
else:
    raise Exception('Element not found')
