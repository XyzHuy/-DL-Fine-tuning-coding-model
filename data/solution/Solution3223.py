import random
import functools
import collections
import string
import math
import datetime


from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        # Calculate the minimum length of the final string
        return sum(1 if x & 1 else 0 for x in cnt.values()) + sum(2 for x in cnt.values() if x > 1 and x % 2 == 0)

def minimumLength(s: str) -> int:
    return Solution().minimumLength(s)