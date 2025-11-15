import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        cnt1 = Counter()
        cnt2 = Counter()
        for a, b in zip(A, B):
            cnt1[a] += 1
            cnt2[b] += 1
            t = sum(min(v, cnt2[x]) for x, v in cnt1.items())
            ans.append(t)
        return ans

def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    return Solution().findThePrefixCommonArray(A, B)