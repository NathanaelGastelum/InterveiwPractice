# Question 1.6

# input: uncompressed string
# output: compressed string

def compress_string(string):
    str_builder = []

    count = 1
    current_char = string[1]
    for c in range(1, len(string)):
        if string[c] == current_char:
            count += 1
        else:
            str_builder += [current_char, str(count)]
            count = 1
            current_char = string[c]
    str_builder += [current_char, str(count)]

    if len(str_builder) >= len(string):
        return string

    return "".join(str_builder)


def decompress_string(string):
    state = 0
    current_char = None
    count = 0
    str_builder = []

    i = 0
    while i < len(string):
        c = string[i]
        if state == 0:
            current_char = c
            state = 1
            count = 0
            i += 1
        else:
            if str.isnumeric(c):
                count = count * 10 + int(c)
                i += 1
            else:
                state = 0
                str_builder += [current_char for _ in range(count)]
    str_builder += [current_char for _ in range(count)]
    
    return "".join(str_builder)


# encoder test
string = "aaabbcccc"
actual = compress_string(string)
expected = "a3b2c4"
assert actual == expected, f"actual: {actual} expected: {expected}"

string = "aaabbaa"
actual = compress_string(string)
expected = "a3b2a2"
assert actual == expected, f"actual: {actual} expected: {expected}"

string = "aaa"
actual = compress_string(string)
expected = "a3"
assert actual == expected, f"actual: {actual} expected: {expected}"


# decoder test
string = "a3b2c4"
actual = decompress_string(string)
expected = "aaabbcccc"
assert actual == expected, f"actual: {actual} expected: {expected}"
