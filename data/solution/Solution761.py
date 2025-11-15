import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base case: if the string is empty or has length 1, return it as is
        if len(s) <= 1:
            return s
        
        # This will store the special substrings
        specials = []
        balance = 0
        start = 0
        
        # Iterate over the string to find special substrings
        for i, char in enumerate(s):
            if char == '1':
                balance += 1
            else:
                balance -= 1
            
            # When balance is 0, we have found a special substring
            if balance == 0:
                # Recursively make the inner part of the substring the largest special
                special_inner = self.makeLargestSpecial(s[start + 1:i])
                # Form the special substring and add it to the list
                specials.append('1' + special_inner + '0')
                # Move the start to the next character after the current special substring
                start = i + 1
        
        # Sort the special substrings in reverse lexicographical order
        specials.sort(reverse=True)
        
        # Join the sorted special substrings to form the largest special string
        return ''.join(specials)

def makeLargestSpecial(s: str) -> str:
    return Solution().makeLargestSpecial(s)