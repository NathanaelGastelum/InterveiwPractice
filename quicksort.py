# Quicksort Implementation Attempt
# Chooses a section of a list and a pivot, moves everything in the section
# based on its relation to the pivot

def quicksort(lst, low, high):
    if len(lst) == 1 or len(lst) == 0: return

    # Select median pivot and move to end of list
    midpoint = (high - low) // 2
    lst[midpoint], lst[high-1] = lst[high-1], lst[midpoint]
    pivot = lst[-1]

    # i keeps track of how many elements have been moved
    i = 0
    for j in range(low, high):
        if lst[j] < pivot:
            lst.insert(i, lst.pop(j))
            i += 1

    # Move pivot back to correct location, only needed if strict inequality on the left
    lst.insert(i, lst.pop(high-1))

    # Recrusion on left and right partitions
    quicksort(lst, low, i)
    quicksort(lst, i, high)

test_lst = [5,1,3,4,2]
quicksort(test_lst, 0, len(test_lst))
actual = test_lst
expected = [1,2,3,4,5]
assert actual == expected, f"actual: {actual} expected: {expected}"