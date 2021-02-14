def quicksort(items):
    """Quick sort in Python

    >>> quicksort([])
    []

    >>> quicksort([2,1])
    [1, 2]

    >>> quicksort([6,1,4,2,3,5])
    [1, 2, 3, 4, 5, 6]
    """
    if len(items) <= 1:
        return items

    pivot = items.pop();
    low = [low for low in items if low < pivot]
    high = [high for high in items if high >= pivot]

    return quicksort(low) + [pivot] + quicksort(high)

if __name__ == "__main__":
    import doctest
    doctest.testmod()