import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from bisect import bisect_right
from string import ascii_lowercase
from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            cnt = Counter(s)
            return next(cnt[c] for c in ascii_lowercase if cnt[c])

        n = len(words)
        nums = sorted(f(w) for w in words)
        return [n - bisect_right(nums, f(q)) for q in queries]

def numSmallerByFrequency(queries: List[str], words: List[str]) -> List[int]:
    return Solution().numSmallerByFrequency(queries, words)