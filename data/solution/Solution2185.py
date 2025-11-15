import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

def prefixCount(words: List[str], pref: str) -> int:
    return Solution().prefixCount(words, pref)