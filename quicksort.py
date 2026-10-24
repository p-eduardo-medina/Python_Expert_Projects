def quicksort_readable(arr):
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three subsets
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quicksort_readable(left) + middle + quicksort_readable(right)


print(quicksort_readable([3, 6, 8, 10, 1, 2, 1]))