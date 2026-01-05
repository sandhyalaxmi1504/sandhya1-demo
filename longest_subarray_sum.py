def longest_subarray_with_sum(arr, k):
    """
    Finds the length of the longest subarray with sum equal to k.
    Works for both positive and negative numbers.
    """
    prefix_sum = 0
    sum_index = {}
    max_len = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If prefix_sum itself equals k
        if prefix_sum == k:
            max_len = i + 1

        # If (prefix_sum - k) seen before
        if (prefix_sum - k) in sum_index:
            max_len = max(max_len, i - sum_index[prefix_sum - k])

        # Store first occurrence only
        if prefix_sum not in sum_index:
            sum_index[prefix_sum] = i

    return max_len


arr = [1, -1, 5, -2, 3]
k = 3
print("Length of longest subarray:", longest_subarray_with_sum(arr, k))
