def merge_sort(items):
    # Base case
    if len(items) <= 1:
        return items

    mid = len(items)//2

    l = items[:mid]
    r = items[mid:]

    merge_sort(l)
    merge_sort(r)

    i = 0
    j = 0
    k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            items[k] = l[i]
            i += 1
        else:
            items[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        items[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        items[k] = r[j]
        j += 1
        k += 1

    return items
if __name__ == "__main__":
    # print(merge([1,5,3,4,2]))
    print(merge_sort([1,5,3,4,2,6,9,8,7,10]))
    print(merge_sort([3,2,1]))
    # assert merge([1,5,3,4,2]) == [1, 2, 3, 4, 5]