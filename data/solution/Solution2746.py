import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        from functools import cache
        
        @cache
        def dp(i, left, right):
            if i == len(words):
                return 0
            
            word = words[i]
            # Option 1: Append word to the current string
            append_length = dp(i + 1, left, word[-1]) + len(word)
            if word[0] == right:
                append_length -= 1
            
            # Option 2: Prepend word to the current string
            prepend_length = dp(i + 1, word[0], right) + len(word)
            if word[-1] == left:
                prepend_length -= 1
            
            return min(append_length, prepend_length)
        
        return dp(1, words[0][0], words[0][-1]) + len(words[0])

def minimizeConcatenatedLength(words: List[str]) -> int:
    return Solution().minimizeConcatenatedLength(words)