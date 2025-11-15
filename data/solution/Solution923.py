import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        n = len(keys)
        result = 0

        # Case 1: all three numbers are the same
        if target % 3 == 0 and target // 3 in count:
            v = target // 3
            if count[v] >= 3:
                result += count[v] * (count[v] - 1) * (count[v] - 2) // 6
                result %= MOD

        # Case 2: two numbers are the same, one is different
        for v1 in keys:
            v2 = target - 2 * v1
            if v1 == v2:
                continue
            if v2 in count and count[v1] >= 2:
                result += count[v1] * (count[v1] - 1) // 2 * count[v2]
                result %= MOD

        # Case 3: all three numbers are different
        for i in range(n):
            for j in range(i + 1, n):
                v3 = target - keys[i] - keys[j]
                if v3 <= keys[j]:
                    continue
                if v3 in count:
                    result += count[keys[i]] * count[keys[j]] * count[v3]
                    result %= MOD

        return result

def threeSumMulti(arr: List[int], target: int) -> int:
    return Solution().threeSumMulti(arr, target)