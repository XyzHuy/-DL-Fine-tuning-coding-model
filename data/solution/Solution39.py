import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, start, path, result):
            if remaining == 0:
                result.append(list(path))
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i, path, result)
                path.pop()
        
        result = []
        candidates.sort()  # Optional: sort to optimize and break early if remaining < 0
        backtrack(target, 0, [], result)
        return result

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    return Solution().combinationSum(candidates, target)