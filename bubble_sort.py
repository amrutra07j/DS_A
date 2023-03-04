
def bubble(lst: list):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

if __name__ == "__main__":
    lst = [2,1,4,3,8,23,12]
    print(bubble(lst))
