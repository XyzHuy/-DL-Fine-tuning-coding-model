import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Count the frequency of each character in all words combined
        char_count = Counter(''.join(words))
        
        # Check if each character's count is divisible by the number of words
        for count in char_count.values():
            if count % len(words) != 0:
                return False
        
        return True

def makeEqual(words: List[str]) -> bool:
    return Solution().makeEqual(words)