import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Create a counter that holds the maximum count of each letter required by any word in words2
        max_count = Counter()
        for word in words2:
            word_count = Counter(word)
            for letter in word_count:
                max_count[letter] = max(max_count[letter], word_count[letter])
        
        # Check each word in words1 to see if it satisfies the max_count requirements
        universal_words = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[letter] >= max_count[letter] for letter in max_count):
                universal_words.append(word)
        
        return universal_words

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    return Solution().wordSubsets(words1, words2)