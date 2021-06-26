# Question 17.14

import random

# O(n log n), can be done faster with Max Heap or selection rank
def smallest_k(lst, k):
    lst.sort()
    result = [lst[i] for i in range(0, k)]
    return result

actual = smallest_k([3,4,2,5,1], 3)
expected = [1,2,3]
assert actual == expected, f"{actual}"


# Selection rank Solution (if elements are unique)
def smallest_k_selection(lst, k):
    threshold = rankf(lst, k - 1)
    smallest = [0 for x in range(k)]
    count = 0

    for a in lst:
        if a < threshold:
            smallest[count] = a
            count += 1

    return smallest

def rankf(lst, rank, left=None, right=None):
    if left == None: left = 0
    if right == None: right = len(lst)-1

    pivot = lst[random.randint(left, right)] 
    left_end = partition(lst, left, right, pivot)
    left_size = left_end - left + 1
    if rank == left_size - 1:
        return max(lst[left : left_end], default=lst[left])
    elif rank < left_size:
        return rankf(lst, rank, left, left_end)
    else:
        return rankf(lst, rank-left_size, left_end+1, right)

def partition(lst, left, right, pivot):
    while left <= right:
        if lst[left] > pivot:
            # Left is bigger than pivot. Swap it to the right side where we know it should be
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1
        elif lst[right] <= pivot:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
        else:
            left += 1
            right -= 1

    return left - 1

test_lst = [5,1,3,4,2]
actual = smallest_k_selection(test_lst, 3)
expected = [1, 2, 3]
assert actual.sort() == expected, f"actual: {actual} expected: {expected}"

# Testing with duplicates
test_lst = [3, 1, 5, 1, 2, 4]
actual = smallest_k_selection(test_lst, 3)
expected = [1, 2, 3]
assert actual.sort() == expected, f"actual: {actual} expected: {expected}"