import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include candidates[i] in the combination
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        candidates.sort()  # Sort to handle duplicates and make it easier to skip them
        result = []
        backtrack(0, [], target)
        return result

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    return Solution().combinationSum2(candidates, target)