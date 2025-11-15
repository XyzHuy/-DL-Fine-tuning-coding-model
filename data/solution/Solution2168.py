import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        from collections import Counter
        
        def is_valid(counter):
            freq = counter.most_common(1)[0][1]
            return all(v == freq for v in counter.values())
        
        unique_substrings = set()
        
        for start in range(len(s)):
            counter = Counter()
            for end in range(start, len(s)):
                counter[s[end]] += 1
                if is_valid(counter):
                    unique_substrings.add(s[start:end+1])
        
        return len(unique_substrings)

def equalDigitFrequency(s: str) -> int:
    return Solution().equalDigitFrequency(s)