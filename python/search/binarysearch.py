def helper(array, target, left, right):
	if left > right:
		return -1
	mid = (left + right) // 2
	potential_match = array[mid]
	
	if target == potential_match:
		return mid
	elif target < potential_match:
		return helper(array, target, left, mid - 1)
	else:
		return helper(array, target, mid+1, right)

def binary_search(array, target):
	return helper(array, target, 0, len(array)-1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    to_search = 1

    print(binary_search(arr, to_search))