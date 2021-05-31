# Given a line, determine if a point is on the line or not
# inputs: values for m and c in the function of a line (y = m*x + c) tuple point
# output: boolean

def on_line(m, c, point):
    if point[1] == (m * point[0] + c):
        return True

    return False

actual = on_line(3, 2, (1,5))
expected = True
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = on_line(3, 2, (3,5))
expected = False
assert actual == expected, f"actual: {actual} expected: {expected}"