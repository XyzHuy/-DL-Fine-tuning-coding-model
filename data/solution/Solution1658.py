import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        if target == 0:
            return len(nums)
        
        max_len = -1
        current_sum = 0
        seen = {0: -1}  # To handle the case where the subarray starts from index 0
        
        for i, num in enumerate(nums):
            current_sum += num
            if current_sum - target in seen:
                max_len = max(max_len, i - seen[current_sum - target])
            if current_sum not in seen:
                seen[current_sum] = i
        
        return len(nums) - max_len if max_len != -1 else -1

# Example usage:
# sol = Solution()
# print(sol.minOperations([1,1,4,2,3], 5))  # Output: 2
# print(sol.minOperations([5,6,7,8,9], 4))  # Output: -1
# print(sol.minOperations([3,2,20,1,1,3], 10))  # Output: 5

def minOperations(nums: List[int], x: int) -> int:
    return Solution().minOperations(nums, x)