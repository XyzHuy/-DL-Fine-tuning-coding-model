import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(after_removal):
            iterator = iter(after_removal)
            return all(char in iterator for char in p)
        
        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) // 2
            after_removal = list(s)
            for i in removable[:mid]:
                after_removal[i] = ''
            if is_subsequence(after_removal):
                left = mid
            else:
                right = mid - 1
        return left

def maximumRemovals(s: str, p: str, removable: List[int]) -> int:
    return Solution().maximumRemovals(s, p, removable)