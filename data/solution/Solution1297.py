import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import Counter
        
        # Dictionary to count occurrences of substrings
        substring_count = Counter()
        
        # Iterate over the string to extract all possible substrings of length minSize
        for i in range(len(s) - minSize + 1):
            substring = s[i:i + minSize]
            # Check if the substring has unique characters less than or equal to maxLetters
            if len(set(substring)) <= maxLetters:
                substring_count[substring] += 1
        
        # Return the maximum occurrence count, or 0 if no valid substring is found
        return max(substring_count.values(), default=0)

def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    return Solution().maxFreq(s, maxLetters, minSize, maxSize)