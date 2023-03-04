def merge(left, right):
    i = 0
    j = 0
    merge_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1


    while i < len(left):
        merge_list.append(left[i])
        i += 1

    while j < len(right):
        merge_list.append(right[j])
        j += 1

    return merge_list


def merge_split(lst: list):
    if len(lst) == 1:
        return lst
    left = merge_split(lst[0:len(lst)//2])
    right = merge_split(lst[len(lst)//2:])

    return merge(left, right)
if __name__ == "__main__":
    lst = [4, 2, 6, 1, 0]
    print(merge_split(lst))