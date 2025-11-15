import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isDecomposable(self, s: str) -> bool:
        count = 1
        has_length_two = False
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                if count % 3 == 1:
                    return False
                elif count % 3 == 2:
                    if has_length_two:
                        return False
                    has_length_two = True
                count = 1
        
        # Check the last group
        if count % 3 == 1:
            return False
        elif count % 3 == 2:
            if has_length_two:
                return False
            has_length_two = True
        
        return has_length_two

def isDecomposable(s: str) -> bool:
    return Solution().isDecomposable(s)