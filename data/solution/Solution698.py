import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
        # If total sum is not divisible by k, we cannot partition it into k equal subsets
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)  # Sort in descending order to optimize the backtracking process
        
        # If any number is greater than the target, we cannot partition it
        if nums[0] > target:
            return False
        
        # Initialize k buckets
        buckets = [0] * k
        
        def backtrack(index: int) -> bool:
            if index == len(nums):
                # Check if all buckets have the same sum
                return all(bucket == target for bucket in buckets)
            
            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= nums[index]
                
                # If the current bucket is empty, no need to try further empty buckets
                if buckets[i] == 0:
                    break
            
            return False
        
        return backtrack(0)

def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    return Solution().canPartitionKSubsets(nums, k)