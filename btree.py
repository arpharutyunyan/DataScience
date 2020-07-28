import random

def main():
    num=int(input('Which number do you search: '))
    # create list with numbers
    list_nums=random.choices([i for i in range(1000)], k=500)
    # sort lists
    sort_list=sorted_list(list_nums)
    # find number
    find_num_btree(num, sort_list)


def sorted_list(lists):
    # check if list is sorted
    if lists==lists.sort():
        return 
    # if list is not sorted 
    lists.sort()
    return lists


def find_num_btree(number, lists):
    # left border
    left=0
    # right border
    right=len(lists)-1
    while right-left>1:
        # middel is half of list's lengh 
        middel=(left+right)//2
        # if number is smaller than middel number from list
        if number<lists[middel]:
            # right border is middel index
            right=middel-1
        else:
            # left border will be middel index
            left=middel
    # check two borders, because <while> condition >1
    if number==lists[left] or number==lists[right]:
        print(f'Your number {number} exists.')
    else:
        print(f'Your number {number} doesn\'t exist.')


if __name__ == "__main__":
    main()
    