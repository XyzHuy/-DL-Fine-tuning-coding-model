import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Sort words by length, and then lexicographically
        words.sort(key=lambda x: (len(x), x))
        
        # Use a set to store valid words
        valid_words = set()
        longest_word = ""
        
        for word in words:
            # Check if the word can be built one character at a time
            if len(word) == 1 or word[:-1] in valid_words:
                valid_words.add(word)
                # Update the longest word if necessary
                if len(word) > len(longest_word):
                    longest_word = word
        
        return longest_word

def longestWord(words: List[str]) -> str:
    return Solution().longestWord(words)