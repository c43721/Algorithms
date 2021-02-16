def merge_sort(items):
    """Merge sort in Python

    >>> merge_sort([])
    []

    >>> merge_sort([1])
    [1]

    >>> merge_sort([2,1])
    [1, 2]

    >>> merge_sort([6,1,4,2,3,5])
    [1, 2, 3, 4, 5, 6]
    """
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
    import doctest

    doctest.testmod()