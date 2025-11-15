import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter()
        ans = []
        for i in range(len(s) - 10 + 1):
            t = s[i : i + 10]
            cnt[t] += 1
            if cnt[t] == 2:
                ans.append(t)
        return ans

def findRepeatedDnaSequences(s: str) -> List[str]:
    return Solution().findRepeatedDnaSequences(s)