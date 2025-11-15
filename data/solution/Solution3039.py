import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        from collections import Counter
        
        # Count the frequency of each character in the string
        freq = Counter(s)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Create a set of characters that have the maximum frequency
        max_freq_chars = {char for char, count in freq.items() if count == max_freq}
        
        # Traverse the string from the end to the beginning to collect the last occurrence of each max_freq_char
        result = []
        seen = set()
        
        for char in reversed(s):
            if char in max_freq_chars and char not in seen:
                result.append(char)
                seen.add(char)
        
        # The result list contains the characters in reverse order, so reverse it back
        return ''.join(result[::-1])

def lastNonEmptyString(s: str) -> str:
    return Solution().lastNonEmptyString(s)