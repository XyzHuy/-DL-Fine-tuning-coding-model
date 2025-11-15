import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(
            w[0] in 'aeiou' and w[-1] in 'aeiou' for w in words[left : right + 1]
        )

def vowelStrings(words: List[str], left: int, right: int) -> int:
    return Solution().vowelStrings(words, left, right)