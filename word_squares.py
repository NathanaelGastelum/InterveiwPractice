# https://techdevguide.withgoogle.com/resources/former-interview-question-word-squares/#!

# A “word square” is an ordered sequence of K different words of length K that, 
# when written one word per line, reads the same horizontally and vertically. For example:

# BALL
# AREA
# LEAD
# LADY

# In this exercise you're going to create a way to find word squares.
# First, design a way to return true if a given sequence of words is a word square.
# Second, given an arbitrary list of words, return all the possible word squares it contains. Reordering is allowed.

# For example, the input list

# [AREA, BALL, DEAR, LADY, LEAD, YARD]

# should output

# [(BALL, AREA, LEAD, LADY), (LADY, AREA, DEAR, YARD)]

# Finishing the first task should help you accomplish the second task.

from collections import deque


def is_word_square(words):
    for i in range(len(words[0])):
        for j in range(i, len(words)):
            if words[i][j] != words[j][i]:
                # index of the word causing the failure
                return i
    return True

def get_word_squares(words):
    queue = word_queue(words)
    word_squares = []

    for word in words:
        temp_square = [word]
        # initialize temp square
        for i in range(1, len(word)):
            if queue.has_next_word(word[i]):
                temp_square += queue.get_next_word(word[i])
            else:
                break
        
        word_check = is_word_square(temp_square)

        # try alternative words if needed
        while word_check != True:
            if queue.has_next_word(word[i]):
                temp_square[word_check] = queue.get_next_word(word[i])
            else:
                break

            word_check = is_word_square(temp_square)

        if  word_check == True:
            word_squares += temp_square

    return word_squares

class word_queue:
    def __init__(self, words) -> None:
        # create dictionary of queues where the key is the starting letter of words in the queue
        self.queues = {}
        for word in words:
            if word[0] not in self.queues:
                self.queues[word[0]] = deque()
            self.queues[word[0]].append(word)
        
    def get_next_word(self, letter):
        return self.queues[letter].popleft()

    def has_next_word(self, letter):
        if letter not in self.queues:
            return False
        else:
            return len(self.queues[letter]) != 0


# Tests
# is_word_square test
tests = [["BALL", "AREA", "LEAD", "LADY"]]
expected = [True]
for i, test in enumerate(tests):
    assert is_word_square(test) == expected[i], f"Test failed"

# get_word_squares test
tests = [["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]]
expected = [[["BALL", "AREA", "LEAD", "LADY"], ["LADY", "AREA", "DEAR", "YARD"]]]
for i, test in enumerate(tests):
    assert get_word_squares(test) == expected[i], f"Test failed"
