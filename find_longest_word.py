# https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/#!

# The Challenge
# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

# Note: D can appear in any format (list, hash table, prefix tree, etc.

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
# Learning objectives
# This question gives you the chance to practice with algorithms and data structures. 
# It’s also a good example of why careful analysis for Big-O performance is often worthwhile, 
# as is careful exploration of common and worst-case input conditions.

def longest_word(S, D):
    w = ""

    for word in D:
        if is_subsequence(word, S):
            if len(word) > len(w):
                w = word

    return w

def is_subsequence(word, string):
    j = 0
    for i in range(len(word)):
        while string[j] != word[i]:
            j += 1
            if j >= len(string): 
                return False

    return True


# Tests
tests = [["abppplee", ["able", "ale", "apple", "bale", "kangaroo"]]]
expected = ["apple"]
for i in range(len(tests)):
    actual = longest_word(tests[i][0], tests[i][1])
    assert actual == expected[i], f"actual: {actual}"
