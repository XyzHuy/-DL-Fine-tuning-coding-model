import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        mid = len(s) // 2
        count_a = count_b = 0
        
        for i in range(mid):
            if s[i] in vowels:
                count_a += 1
            if s[i + mid] in vowels:
                count_b += 1
        
        return count_a == count_b

def halvesAreAlike(s: str) -> bool:
    return Solution().halvesAreAlike(s)