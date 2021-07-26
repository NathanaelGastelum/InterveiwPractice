# inputs: list to be searched, integer search target
# output: index of search target, or None if target not in list

# Follow Up: What if it's rotated +/- n amount of times?

class BinarySearch:
    def binary_search(self, lst, n):
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
    

    def rotated_binary_search(self, lst, n):
        left_bound = 0
        right_bound = len(lst) - 1
        midpoint = len(lst) // 2

        while left_bound <= right_bound:
            if n == lst[midpoint]: return midpoint
            # logical start is to the left of midpoint
            if lst[left_bound] > lst[midpoint]:
                # n is left of midpoint
                if n < lst[midpoint] or n >= lst[left_bound]:
                    # shift left
                    right_bound = midpoint - 1
                    midpoint = left_bound + (right_bound - left_bound) // 2
                # n is right of midpoint
                else:
                    # shift right
                    left_bound = midpoint + 1
                    midpoint = midpoint = left_bound + (right_bound - left_bound) // 2

            # logical start is to the right of midpoint or not rotated
            else:
                # n is left of midpoint
                if n < lst[midpoint] and n >= lst[left_bound]:
                    right_bound = midpoint - 1
                    midpoint = left_bound + (right_bound - left_bound) // 2
                # n is right of midpoint
                else:
                    left_bound = midpoint + 1
                    midpoint = midpoint = left_bound + (right_bound - left_bound) // 2
        return None

test_class = BinarySearch()
test_fn = test_class.rotated_binary_search
lst = [1,2,3,4,5,6,7,8,9,10]
actual = test_fn(lst, 9)
expected = 8
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 10)
expected = 9
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 2)
expected = 1
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 1)
expected = 0
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 0)
expected = None
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 11)
expected = None
assert actual == expected, f"actual: {actual} expected: {expected}"

# rotated list tests
test_class = BinarySearch()
test_fn = test_class.rotated_binary_search
lst = [7,8,9,10,1,2,3,4,5,6]
actual = test_fn(lst, 9)
expected = 2
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 2)
expected = 5
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 6)
expected = 9
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 7)
expected = 0
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 0)
expected = None
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 11)
expected = None
assert actual == expected, f"actual: {actual} expected: {expected}"

lst = [8,9,10,1,2,3,4,5,6,7]
actual = test_fn(lst, 9)
expected = 1
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 4)
expected = 6
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 7)
expected = 9
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 8)
expected = 0
assert actual == expected, f"actual: {actual} expected: {expected}"

lst = [3,4,5,6,7,8,9,10,1,2]
actual = test_fn(lst, 5)
expected = 2
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 9)
expected = 6
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 2)
expected = 9
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = test_fn(lst, 3)
expected = 0
assert actual == expected, f"actual: {actual} expected: {expected}"
