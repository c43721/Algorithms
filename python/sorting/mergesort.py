def merge(items):
    # Base case
    if len(items) <= 1:
        return items
    
    # Declare sub lists left and right to call recursive sort
    left = []
    right = []

    for i in items:
        left.append(i) if i < len(items) / 2 else right.append(i)
    

    sorted_left = merge(left)
    sorted_right = merge(right)
    # the final merge, merge the sorted left and right, and call merge on that...
    return sorted_left + sorted_right

if __name__ == "__main__":
    # print(merge([1,5,3,4,2]))
    print(merge([1,5,3,4,2,6,9,8,7,10]))
    # assert merge([1,5,3,4,2]) == [1, 2, 3, 4, 5]

    print(True)