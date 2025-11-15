import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def count_differing_by_one(start_s, start_t):
            count = 0
            diff_count = 0
            for i in range(min(len(s) - start_s, len(t) - start_t)):
                if s[start_s + i] != t[start_t + i]:
                    diff_count += 1
                if diff_count > 1:
                    break
                if diff_count == 1:
                    count += 1
            return count
        
        total_count = 0
        for i in range(len(s)):
            for j in range(len(t)):
                total_count += count_differing_by_one(i, j)
        
        return total_count

def countSubstrings(s: str, t: str) -> int:
    return Solution().countSubstrings(s, t)