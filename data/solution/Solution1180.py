import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countLetters(self, s: str) -> int:
        total = 0
        current_char = s[0]
        current_count = 1
        
        for i in range(1, len(s)):
            if s[i] == current_char:
                current_count += 1
            else:
                total += (current_count * (current_count + 1)) // 2
                current_char = s[i]
                current_count = 1
        
        # Add the count for the last group of characters
        total += (current_count * (current_count + 1)) // 2
        
        return total

def countLetters(s: str) -> int:
    return Solution().countLetters(s)