from search import binary_search

arr = ['B', 'E', 'K', 'J', 'A', 'U', 'P']
element = 'J'

def insert_sort (arr):
    # symbols sorted base on ord(ascii symbols)
    for i in range(1, len(arr)):
        j = i
        while j >0 and arr[j] <= arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr

sorted_arr = insert_sort(arr)

index = binary_search(sorted_arr, element)

print(index)
