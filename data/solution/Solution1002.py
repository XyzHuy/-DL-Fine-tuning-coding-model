import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        # Initialize the counter with the first word
        common_count = Counter(words[0])
        
        # Intersect with the counters of the remaining words
        for word in words[1:]:
            common_count &= Counter(word)
        
        # Convert the counter to a list of characters
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result

def commonChars(words: List[str]) -> List[str]:
    return Solution().commonChars(words)