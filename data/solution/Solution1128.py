import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Use a dictionary to count occurrences of each normalized domino
        count = defaultdict(int)
        result = 0
        
        for domino in dominoes:
            # Normalize the domino by sorting the pair
            normalized = tuple(sorted(domino))
            # If we have seen this domino before, it can form pairs with all previous occurrences
            result += count[normalized]
            # Increment the count of this domino
            count[normalized] += 1
        
        return result

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    return Solution().numEquivDominoPairs(dominoes)