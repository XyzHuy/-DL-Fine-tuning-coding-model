import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        result = 0
        
        # Calculate the number of substrings for each character
        for count in char_count.values():
            # For each character that appears 'count' times, the number of substrings
            # that can be formed is the sum of the first 'count' natural numbers
            result += count * (count + 1) // 2
        
        return result

def numberOfSubstrings(s: str) -> int:
    return Solution().numberOfSubstrings(s)