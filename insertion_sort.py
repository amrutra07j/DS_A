def insertion(lst:list):
    for i in range(1, len(lst)):
        for j in range(i-1, -1, -1):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
                i=j
            else:
                break
    return lst

if __name__ == "__main__":
    lst = [99, 2,1,4,3,8,23,12,100]
    print(insertion(lst))