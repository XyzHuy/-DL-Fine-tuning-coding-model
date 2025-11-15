import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Count the frequency of each character in chars
        chars_count = Counter(chars)
        total_length = 0
        
        for word in words:
            # Count the frequency of each character in the current word
            word_count = Counter(word)
            # Check if the word can be formed by the characters in chars
            if all(word_count[char] <= chars_count[char] for char in word_count):
                total_length += len(word)
        
        return total_length

def countCharacters(words: List[str], chars: str) -> int:
    return Solution().countCharacters(words, chars)