def binary_search(arr, x):
    """
    Performs binary search on a sorted array.
    Returns index if found, else -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(binary_search([1, 2, 3, 4, 5], 4))

