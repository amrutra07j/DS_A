def selection(lst:list):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

if __name__ == "__main__":
    lst = [99, 2,1,4,3,8,23,12,100]
    print(selection(lst))

