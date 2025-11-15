import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count

def numOfStrings(patterns: List[str], word: str) -> int:
    return Solution().numOfStrings(patterns, word)