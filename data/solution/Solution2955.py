import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # prefix_count[i][c] will store the count of character c up to index i
        prefix_count = [[0] * 26 for _ in range(n + 1)]
        
        # Fill the prefix count array
        for i in range(n):
            for c in range(26):
                prefix_count[i + 1][c] = prefix_count[i][c]
            prefix_count[i + 1][ord(s[i]) - ord('a')] += 1
        
        ans = []
        for li, ri in queries:
            count_same_end = 0
            for c in range(26):
                count = prefix_count[ri + 1][c] - prefix_count[li][c]
                if count > 0:
                    # Number of same-end substrings for this character
                    count_same_end += count * (count + 1) // 2
            ans.append(count_same_end)
        
        return ans

def sameEndSubstringCount(s: str, queries: List[List[int]]) -> List[int]:
    return Solution().sameEndSubstringCount(s, queries)