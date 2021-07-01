# Question 1.6
# TODO: write a decoder for the encoded string

# input: uncompressed string
# output: compressed string

def compress_string(string):
    char_cache = {}

    for c in string:
        if c not in char_cache:
            char_cache[c] = 0
        char_cache[c] += 1

    if len(char_cache) * 2 >= len(string):
        return string

    str_builder = []
    for c in char_cache.items():
        str_builder.append(c[0])
        str_builder.append(str(c[1]))

    return "".join(str_builder)


string = "aaabbcccc"
actual = compress_string(string)
expected = "a3b2c4"
assert actual == expected, f"actual: {actual} expected: {expected}"