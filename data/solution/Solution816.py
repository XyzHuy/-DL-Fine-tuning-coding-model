import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> List[str]:
            n = len(frag)
            ans = []
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if (not left.startswith('0') or left == '0') and (not right.endswith('0')):
                    if right:
                        ans.append(left + '.' + right)
                    else:
                        ans.append(left)
            return ans
        
        s = s[1:-1]  # remove the parentheses
        n = len(s)
        res = []
        
        for i in range(1, n):
            left = s[:i]
            right = s[i:]
            for candidate_left in make(left):
                for candidate_right in make(right):
                    res.append(f"({candidate_left}, {candidate_right})")
        
        return res

def ambiguousCoordinates(s: str) -> List[str]:
    return Solution().ambiguousCoordinates(s)