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

from collections import deque

def longest_word(S, D):
    # sort in order to avoid checking smaller words first
    D.sort(key=str.__len__, reverse=True)

    for word in D:
        if is_subsequence(word, S):
            return word

    return None


# brute force? at first I thought it was more optimal than the greedy function, but I see now that it's 2^n each time the function is called
# Maybe this would be the best option for a class that gets multiple queries?
def all_subsequences(string):
    subsequences = set()
    for i in range(len(string)):
        queue = deque(string[i])

        while queue:
            current = queue.popleft()
            subsequences.add("".join(current))
            for j in range(i, len(string)):
                queue.append(current + string[j])

    return subsequences

# Apparently this is a greedy implementation?
def is_subsequence(word, string):
    j = 0
    for i in range(len(word)):
        # TODO: improve by not scanning every letter in string
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
