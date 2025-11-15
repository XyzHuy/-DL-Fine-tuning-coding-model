import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start by assuming the whole first string is the common prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # Reduce the prefix length until it matches the start of the string
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
            # If at any point the prefix becomes empty, return immediately
            if not prefix:
                return ""
        
        return prefix

def longestCommonPrefix(strs: List[str]) -> str:
    return Solution().longestCommonPrefix(strs)