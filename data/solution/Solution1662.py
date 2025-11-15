import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    return Solution().arrayStringsAreEqual(word1, word2)