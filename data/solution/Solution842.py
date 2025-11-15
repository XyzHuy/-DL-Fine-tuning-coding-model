import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def is_valid(num_str):
            return len(num_str) == 1 or (num_str[0] != '0' and int(num_str) < 2**31)
        
        def backtrack(start, path):
            if start == len(num) and len(path) > 2:
                return path
            
            for end in range(start + 1, len(num) + 1):
                candidate = num[start:end]
                if not is_valid(candidate):
                    continue
                if len(path) >= 2 and int(candidate) != path[-1] + path[-2]:
                    continue
                path.append(int(candidate))
                if backtrack(end, path):
                    return path
                path.pop()
            return []
        
        return backtrack(0, [])

def splitIntoFibonacci(num: str) -> List[int]:
    return Solution().splitIntoFibonacci(num)