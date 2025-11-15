import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        
        # Count the frequency of each letter in both words
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Get all unique letters in both words
        all_letters = set(count1.keys()).union(set(count2.keys()))
        
        # Check the difference in frequencies for each letter
        for letter in all_letters:
            if abs(count1[letter] - count2[letter]) > 3:
                return False
        
        return True

def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    return Solution().checkAlmostEquivalent(word1, word2)