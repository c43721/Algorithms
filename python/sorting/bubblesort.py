def bubble_sort(array):
    """Bubble sort in Python

    >>> bubble_sort([])
    []

    >>> bubble_sort([2,1])
    [1, 2]

    >>> bubble_sort([6,1,4,2,3,5])
    [1, 2, 3, 4, 5, 6]
    """
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                is_sorted=False
                array[i], array[i+1] = array[i+1], array[i]
    return array

if __name__ == "__main__":
    import doctest

    doctest.testmod()