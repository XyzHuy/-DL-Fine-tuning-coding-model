import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            return str2.startswith(str1) and str2.endswith(str1)
        
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        
        return count

def countPrefixSuffixPairs(words: List[str]) -> int:
    return Solution().countPrefixSuffixPairs(words)