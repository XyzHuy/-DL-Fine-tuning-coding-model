import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        seen = {}
        
        for word in words:
            for prev_word, freq in seen.items():
                if word.startswith(prev_word) and word.endswith(prev_word):
                    count += freq
            if word in seen:
                seen[word] += 1
            else:
                seen[word] = 1
        
        return count

def countPrefixSuffixPairs(words: List[str]) -> int:
    return Solution().countPrefixSuffixPairs(words)