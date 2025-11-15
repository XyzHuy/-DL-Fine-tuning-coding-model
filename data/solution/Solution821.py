import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [float('inf')] * n
        
        # First pass: left to right
        prev = None
        for i in range(n):
            if s[i] == c:
                prev = i
            if prev is not None:
                answer[i] = i - prev
        
        # Second pass: right to left
        prev = None
        for i in range(n-1, -1, -1):
            if s[i] == c:
                prev = i
            if prev is not None:
                answer[i] = min(answer[i], prev - i)
        
        return answer

def shortestToChar(s: str, c: str) -> List[int]:
    return Solution().shortestToChar(s, c)