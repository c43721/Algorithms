def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

def helper(array, start, end):
	if start >= end:
		return
	pivot = start
	left = start+1
	right = end
	while right >= left:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(array, left, right)
		if array[left] <= array[pivot]:
			left+=1
		if array[right] >= array[pivot]:
			right-=1
	swap(array, pivot, right)

    # Optimize to get nlogn time
	leftIsSmaller = right - 1 - start < end - (right+1)
	if leftIsSmaller:
		helper(array, start, right-1)
		helper(array, right+1, end)
	else:
		helper(array, right+1, end)
		helper(array, start, right-1)

def quick_sort(items):
    """Quick sort in Python

    >>> quick_sort([])
    []

    >>> quick_sort([2,1])
    [1, 2]

    >>> quick_sort([6,1,4,2,3,5])
    [1, 2, 3, 4, 5, 6]
    """
    helper(items, 0, len(items)-1)
    return items

if __name__ == "__main__":
    import doctest
    doctest.testmod()