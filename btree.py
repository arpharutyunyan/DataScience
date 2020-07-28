import random

def main():
    
    # create list with numbers
    list_nums=random.choices([i for i in range(1000)], k=500)
    # sort lists
    sort_list=sorted_list(list_nums)
    num=int(input('Which number do you search: '))
    # print(sort_list)
    find_num_btree(num, sort_list)


def sorted_list(lists):
    # check if list is sorted
    if lists==lists.sort():
        return 
    lists.sort()
    return lists


def find_num_btree(number, lists):
    l=0
    r=len(lists)-1
    while r-l>1:
        m=(l+r)//2
        if number<lists[m]:
            r=m-1
        else:
            l=m
    if number==lists[l] or number==lists[r]:
        print(f'Your number {number} exists.')
    else:
        print(f'Your number {number} doesn\'t exist.')


if __name__ == "__main__":
    main()
    