import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the rows of the keyboard
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        # Function to check if a word can be typed using one row
        def can_type_with_one_row(word):
            # Convert word to lowercase
            word_set = set(word.lower())
            # Check if the word is a subset of any row
            return word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3)
        
        # Filter words that can be typed with one row
        return [word for word in words if can_type_with_one_row(word)]

# Example usage:
# solution = Solution()
# print(solution.findWords(["Hello","Alaska","Dad","Peace"]))  # Output: ["Alaska","Dad"]
# print(solution.findWords(["omk"]))  # Output: []
# print(solution.findWords(["adsdf","sfd"]))  # Output: ["adsdf","sfd"]

def findWords(words: List[str]) -> List[str]:
    return Solution().findWords(words)