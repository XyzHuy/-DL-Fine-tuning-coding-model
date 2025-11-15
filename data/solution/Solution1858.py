import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Create a set of words for O(1) lookups
        word_set = set(words)
        # Initialize the result to an empty string
        longest_word = ""
        
        for word in words:
            # Check if all prefixes of the word are in the set
            if all(prefix in word_set for prefix in (word[:i] for i in range(1, len(word)))):
                # If the word is longer than the current longest, or lexicographically smaller if the same length
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        
        return longest_word

def longestWord(words: List[str]) -> str:
    return Solution().longestWord(words)