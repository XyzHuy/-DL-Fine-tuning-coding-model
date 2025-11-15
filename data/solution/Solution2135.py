import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        s = {sum(1 << (ord(c) - 97) for c in w) for w in startWords}
        ans = 0
        for w in targetWords:
            x = sum(1 << (ord(c) - 97) for c in w)
            for c in w:
                if x ^ (1 << (ord(c) - 97)) in s:
                    ans += 1
                    break
        return ans

def wordCount(startWords: List[str], targetWords: List[str]) -> int:
    return Solution().wordCount(startWords, targetWords)