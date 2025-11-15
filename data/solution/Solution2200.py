import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        k_distant_indices = set()
        
        for i in range(n):
            if nums[i] == key:
                left = max(0, i - k)
                right = min(n, i + k + 1)
                for j in range(left, right):
                    k_distant_indices.add(j)
        
        return sorted(k_distant_indices)

def findKDistantIndices(nums: List[int], key: int, k: int) -> List[int]:
    return Solution().findKDistantIndices(nums, key, k)