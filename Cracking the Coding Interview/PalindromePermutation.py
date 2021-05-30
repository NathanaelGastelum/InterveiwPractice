# Question 1.4

# Input(s): String
# Output: Boolean

def is_palindrome_permutation(str):
    # Converting to set doesn't work, could have any number of the same character?
    '''
    temp_set = {x for x in str if x != " "}

    # Even/odd check to account for potential single letter
    if len(temp_set) % 2 == 0:
        if len(temp_set) == len(str) * 2:
            return True

    else:
        if len(temp_set) == len(str) * 2 + 1:
            return True
    '''
    char_count_dict = {}

    for c in str:
        if c == " ":
            continue
        # Need lower() to make case insensitive
        if c.lower() not in char_count_dict:
            char_count_dict[c.lower()] = 0
        char_count_dict[c.lower()] += 1
    
    count = 0
    for x in char_count_dict.values():
        if x % 2 != 0:
            count += 1
            if count > 1:
                return False

    return True

actual = is_palindrome_permutation("tact coa")
expected = True
assert actual == expected, f"actual: {actual} expected: {expected}"

actual = is_palindrome_permutation("Tact Coa")
expected = True
assert actual == expected, f"actual: {actual} expected: {expected}"