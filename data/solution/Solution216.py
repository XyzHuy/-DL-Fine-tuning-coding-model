import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, target, k):
            if k == 0:
                if target == 0:
                    result.append(path)
                return
            for i in range(start, 10):
                if i > target:
                    break
                backtrack(i + 1, path + [i], target - i, k - 1)
        
        result = []
        backtrack(1, [], n, k)
        return result

# Example usage:
# sol = Solution()
# print(sol.combinationSum3(3, 7))  # Output: [[1,2,4]]
# print(sol.combinationSum3(3, 9))  # Output: [[1,2,6],[1,3,5],[2,3,4]]
# print(sol.combinationSum3(4, 1))  # Output: []

def combinationSum3(k: int, n: int) -> List[List[int]]:
    return Solution().combinationSum3(k, n)