arr = [4, 7, 8, 3, 2, 9, 0]

def insert_sort (lis):
    for i in range(1, len(arr)):
        j = i
        while j >0 and arr[j] <= arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return lis

print(insert_sort(arr))