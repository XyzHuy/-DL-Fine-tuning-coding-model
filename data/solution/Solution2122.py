import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        # Try each possible k
        for i in range(1, n):
            k = (nums[i] - nums[0]) // 2
            if k <= 0 or nums[i] - nums[0] != 2 * k:
                continue
            
            count = Counter(nums)
            arr = []
            
            # Try to form the original array
            for x in nums:
                if count[x] == 0:
                    continue
                if count[x + 2 * k] == 0:
                    break
                arr.append(x + k)
                count[x] -= 1
                count[x + 2 * k] -= 1
            
            if len(arr) == n // 2:
                return arr
        
        return []

# Example usage:
# sol = Solution()
# print(sol.recoverArray([2,10,6,4,8,12]))  # Output: [3,7,11]
# print(sol.recoverArray([1,1,3,3]))        # Output: [2,2]
# print(sol.recoverArray([5,435]))           # Output: [220]

def recoverArray(nums: List[int]) -> List[int]:
    return Solution().recoverArray(nums)