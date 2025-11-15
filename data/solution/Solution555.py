import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        # Reverse each string if its reverse is lexicographically larger
        strs = [max(s, s[::-1]) for s in strs]
        
        # Initialize the result with the smallest possible string
        result = ""
        
        # Try each string as the starting point of the loop
        for i in range(len(strs)):
            # Form the main part of the string without the current string
            main_part = "".join(strs[i+1:]) + "".join(strs[:i])
            
            # Try both the original and reversed version of the current string
            for s in (strs[i], strs[i][::-1]):
                # Try cutting at each position in the current string
                for j in range(len(s) + 1):
                    # Form the candidate string by concatenating the parts
                    candidate = s[j:] + main_part + s[:j]
                    # Update the result if the candidate is lexicographically larger
                    if candidate > result:
                        result = candidate
        
        return result

def splitLoopedString(strs: List[str]) -> str:
    return Solution().splitLoopedString(strs)