import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def beautySum(self, s: str) -> int:
        def calculate_beauty(counter):
            max_freq = max(counter.values())
            min_freq = min(counter.values())
            return max_freq - min_freq

        total_beauty = 0
        n = len(s)
        
        for i in range(n):
            counter = {}
            for j in range(i, n):
                if s[j] in counter:
                    counter[s[j]] += 1
                else:
                    counter[s[j]] = 1
                if len(counter) > 1:
                    total_beauty += calculate_beauty(counter)
        
        return total_beauty

def beautySum(s: str) -> int:
    return Solution().beautySum(s)