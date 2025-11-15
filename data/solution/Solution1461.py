import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # We need to check if all possible binary codes of length k are substrings of s.
        # There are 2^k possible binary codes of length k.
        # We can use a set to store all unique substrings of length k found in s.
        
        unique_substrings = set()
        
        # Iterate over the string to extract all substrings of length k
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            unique_substrings.add(substring)
        
        # Check if we have found all 2^k possible binary codes of length k
        return len(unique_substrings) == 2 ** k

def hasAllCodes(s: str, k: int) -> bool:
    return Solution().hasAllCodes(s, k)