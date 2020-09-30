import math

arr = [4, 7, 8, 3, 2, 9, 0]
sort_arr = [0, 2, 3, 4, 7, 8, 9]
data = 2

def liner_search (lis, element):
    for i in range(len(lis)):
        if lis[i] == element:
            return i
    return -1


def binary_search (ys, element):
    first = 0
    last = len(ys) - 1
    index = -1

    while (first<= last) and (index == -1):
        m = (first + last)//2
        if ys[m] == element:
            index = m
        else:
            if element < ys[m]:
                last = m-1
            else:
                first = m+1
    return index
        

def exponential_search (ys, element):
    if ys[0] == element:
        return 0
    
    index = 1
    while index < len(ys) and ys[index]<=element:
        index = index * 2

    return binary_search(ys[:min(index, len(ys))], element)


def jump_search (ys, element):
    lenght = len(ys)
    jump = int(math.sqrt(lenght))
    left = 0
    right = 0
    while left < lenght and ys[left] <= element:
        right = min(lenght-1, left + jump)
        if ys[left] <= element and ys[right] >= element:
            break
        left +=jump
    if left >= lenght or ys[left] > element:
        return -1
    right = min(lenght-1, right)
    l = left
    while l <= right and ys[l] <= element:
        if ys[l] == element:
            return l
        l += 1
    return -1

# print('=======', jump_search(sort_arr, data))