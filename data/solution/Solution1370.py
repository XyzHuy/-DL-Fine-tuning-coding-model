import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        
        # Count the frequency of each character
        char_count = Counter(s)
        result = []
        unique_chars = sorted(char_count.keys())
        
        while len(result) < len(s):
            # Step 1 to 3: Remove smallest characters in ascending order
            for char in unique_chars:
                if char_count[char] > 0:
                    result.append(char)
                    char_count[char] -= 1
            
            # Step 4 to 6: Remove largest characters in descending order
            for char in reversed(unique_chars):
                if char_count[char] > 0:
                    result.append(char)
                    char_count[char] -= 1
        
        return ''.join(result)

def sortString(s: str) -> str:
    return Solution().sortString(s)