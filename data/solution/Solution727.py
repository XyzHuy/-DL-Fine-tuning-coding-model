import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        min_len = float('inf')
        start_index = -1
        
        def find_next_subsequence(start):
            j = 0
            for i in range(start, m):
                if s1[i] == s2[j]:
                    j += 1
                    if j == n:
                        return i
            return -1
        
        i = 0
        while i < m:
            if s1[i] == s2[0]:
                end = find_next_subsequence(i)
                if end != -1:
                    if end - i + 1 < min_len:
                        min_len = end - i + 1
                        start_index = i
                    # Move i forward to find the next starting point of the subsequence
                    i += 1
                else:
                    break
            else:
                i += 1
        
        if start_index == -1:
            return ""
        else:
            return s1[start_index:start_index + min_len]

def minWindow(s1: str, s2: str) -> str:
    return Solution().minWindow(s1, s2)