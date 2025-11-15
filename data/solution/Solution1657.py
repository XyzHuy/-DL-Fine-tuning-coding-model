import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If the lengths of the words are different, they cannot be close
        if len(word1) != len(word2):
            return False
        
        # Count the frequency of each character in both words
        from collections import Counter
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # If the sets of characters in both words are different, they cannot be close
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # If the frequency of character occurrences are the same, they can be transformed into each other
        return sorted(count1.values()) == sorted(count2.values())

def closeStrings(word1: str, word2: str) -> bool:
    return Solution().closeStrings(word1, word2)