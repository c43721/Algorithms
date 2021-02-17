def quick_sort(items):
    """Quick sort in Python

    >>> quick_sort([])
    []

    >>> quick_sort([2,1])
    [1, 2]

    >>> quick_sort([6,1,4,2,3,5])
    [1, 2, 3, 4, 5, 6]
    """
    if len(items) <= 1:
        return items

    pivot = items.pop()
    low = [low for low in items if low < pivot]
    high = [high for high in items if high >= pivot]

    return quick_sort(low) + [pivot] + quick_sort(high)

if __name__ == "__main__":
    import doctest
    doctest.testmod()