import random
def pivot(lst, pivot_index, end_index):
    swap = pivot_index
    for i in range(swap+1, end_index+1):
        if lst[pivot_index] > lst[i]:
            swap += 1
            lst[swap], lst[i] = lst[i], lst[swap]
    lst[pivot_index], lst[swap] = lst[swap], lst[pivot_index]
    return swap


def sort_quick(lst, l_index, r_index):
    if l_index < r_index:
        piv = pivot(lst, l_index, r_index)
        sort_quick(lst, l_index, piv-1)
        sort_quick(lst, piv+1, r_index)
    return lst

def quick(lst):
    return sort_quick(lst, 0, len(lst)-1)

if __name__ == "__main__":
    lst = [random.randint(1, 1000) for i in range(1, 1000)]
    print(quick(lst))
