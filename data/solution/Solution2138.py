import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s), k):
            group = s[i:i+k]
            if len(group) < k:
                group += fill * (k - len(group))
            result.append(group)
        return result

def divideString(s: str, k: int, fill: str) -> List[str]:
    return Solution().divideString(s, k, fill)