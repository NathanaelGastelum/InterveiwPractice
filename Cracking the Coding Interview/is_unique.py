def isUnique(string):
    charSet = set()

    for c in string:
        if c in charSet:
            return False
        else:
            charSet.add(c)
    return True

string = "worldw"
print(isUnique(string))

# if not allowed to use other data structures, sort the string (with sort(string)) and then check for matching adjacent characters