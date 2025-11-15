import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove all dashes and convert to uppercase
        s = s.replace('-', '').upper()
        
        # Calculate the length of the first group
        first_group_length = len(s) % k
        if first_group_length == 0:
            first_group_length = k
        
        # Create the first group
        result = s[:first_group_length]
        
        # Create the remaining groups
        for i in range(first_group_length, len(s), k):
            if result:
                result += '-'
            result += s[i:i+k]
        
        return result

def licenseKeyFormatting(s: str, k: int) -> str:
    return Solution().licenseKeyFormatting(s, k)