import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        # If str2 contains all 26 letters, it's impossible to convert
        if len(set(str2)) == 26:
            return False
        
        # Dictionary to hold the mapping from characters in str1 to str2
        mapping = {}
        
        for char1, char2 in zip(str1, str2):
            # If we are trying to map char1 to a different character than previously mapped, return False
            if char1 in mapping and mapping[char1] != char2:
                return False
            mapping[char1] = char2
        
        return True

def canConvert(str1: str, str2: str) -> bool:
    return Solution().canConvert(str1, str2)