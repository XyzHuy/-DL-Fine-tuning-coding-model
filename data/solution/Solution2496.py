import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def value_of_string(s: str) -> int:
            if s.isdigit():
                return int(s)
            else:
                return len(s)
        
        return max(value_of_string(s) for s in strs)

def maximumValue(strs: List[str]) -> int:
    return Solution().maximumValue(strs)