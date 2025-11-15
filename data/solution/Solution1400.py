import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible to construct k palindromes
        if k > len(s):
            return False
        
        # If k is equal to the length of the string, each character can be its own palindrome
        if k == len(s):
            return True
        
        # Count the frequency of each character in the string
        from collections import Counter
        char_count = Counter(s)
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # We can form at least odd_count palindromes with the characters that have odd frequencies
        # The remaining characters (with even frequencies) can be distributed to form more palindromes
        # We need at least odd_count palindromes, so k must be at least odd_count
        return k >= odd_count

def canConstruct(s: str, k: int) -> bool:
    return Solution().canConstruct(s, k)