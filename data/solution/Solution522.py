import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            it = iter(t)
            return all(c in it for c in s)
        
        # Sort strings by length in descending order
        strs.sort(key=len, reverse=True)
        
        for i, word in enumerate(strs):
            unique = True
            for j, other_word in enumerate(strs):
                if i != j and is_subsequence(word, other_word):
                    unique = False
                    break
            if unique:
                return len(word)
        
        return -1

def findLUSlength(strs: List[str]) -> int:
    return Solution().findLUSlength(strs)