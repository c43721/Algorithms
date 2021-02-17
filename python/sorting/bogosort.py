from random import randint

def bogo_sort(items):
    """Bogo sort in Python

    >>> bogo_sort([])
    []

    >>> bogo_sort([2,1])
    [1, 2]

    >>> bogo_sort([6,1,4,2,3,5])
    [1, 2, 3, 4, 5, 6]
    """

    if len(items) <= 1:
        return items

    while not is_sorted(items):
        shuffle(items)
    else:
        return items

def is_sorted(items):
    for i in range(len(items)-1):
        if items[i] > items[i+1]: 
            return False
    return True

def shuffle(items):
    for i in range(0, len(items)-1):
        r = randint(0, len(items)-1)
        items[i], items[r] = items[r], items[i]


if __name__ == "__main__":
    import doctest
    doctest.testmod()