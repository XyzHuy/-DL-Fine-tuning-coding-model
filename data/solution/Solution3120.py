import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special_count = 0
        seen_lower = set()
        seen_upper = set()
        
        for char in word:
            if char.islower():
                seen_lower.add(char)
            elif char.isupper():
                seen_upper.add(char.lower())
        
        for char in seen_lower:
            if char in seen_upper:
                special_count += 1
        
        return special_count

def numberOfSpecialChars(word: str) -> int:
    return Solution().numberOfSpecialChars(word)