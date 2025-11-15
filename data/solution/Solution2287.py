import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in s and target
        count_s = Counter(s)
        count_target = Counter(target)
        
        # Initialize the maximum number of copies to a large number
        max_copies = float('inf')
        
        # For each character in the target, calculate how many copies can be made
        for char in count_target:
            if char in count_s:
                max_copies = min(max_copies, count_s[char] // count_target[char])
            else:
                # If any character in target is not in s, we cannot form any copies
                return 0
        
        return max_copies

def rearrangeCharacters(s: str, target: str) -> int:
    return Solution().rearrangeCharacters(s, target)