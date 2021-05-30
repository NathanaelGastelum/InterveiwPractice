# inputs: list to be searched, integer search target
# output: index of search target, or None if target not in list

def binary_search(lst, n):
    left_bound = 0
    right_bound = len(lst) - 1
    midpoint = len(lst) // 2

    while left_bound <= right_bound:
        if n < lst[midpoint]:
            right_bound = midpoint - 1
            midpoint = left_bound + (right_bound - left_bound) // 2
        elif n > lst[midpoint]:
            left_bound = midpoint + 1
            midpoint = left_bound + (right_bound - left_bound) // 2
        else:
            return midpoint
    return None

lst = [1,2,3,4,5,6,7,8,9,10]
actual = binary_search(lst, 9)
expected = 8
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = binary_search(lst, 10)
expected = 9
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = binary_search(lst, 2)
expected = 1
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = binary_search(lst, 1)
expected = 0
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = binary_search(lst, 0)
expected = None
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = binary_search(lst, 11)
expected = None
assert actual == expected, f"actual: {actual} expected: {expected}"