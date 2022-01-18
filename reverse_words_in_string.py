# LeetCode Medium
# https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords(s: str) -> str:
    word_list = s.split()
    # word_list.reverse()
    
    start = 0
    end = len(word_list) - 1
    
    for i in range(len(word_list) // 2):
        word_list[start], word_list[end] = word_list[end], word_list[start]
        start += 1
        end -= 1
    
    return " ".join(word_list)