import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Count the occurrences of each word in both lists
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        # Initialize the result counter
        result = 0
        
        # Iterate through the first counter
        for word, count in count1.items():
            # Check if the word appears exactly once in both counters
            if count == 1 and count2[word] == 1:
                result += 1
        
        return result

def countWords(words1: List[str], words2: List[str]) -> int:
    return Solution().countWords(words1, words2)