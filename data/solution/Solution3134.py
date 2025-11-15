import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def countDistinctSubarrays(nums, k):
            count = 0
            n = len(nums)
            distinct_count = defaultdict(int)
            left = 0
            for right in range(n):
                distinct_count[nums[right]] += 1
                while len(distinct_count) > k:
                    distinct_count[nums[left]] -= 1
                    if distinct_count[nums[left]] == 0:
                        del distinct_count[nums[left]]
                    left += 1
                count += right - left + 1
            return count
        
        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if countDistinctSubarrays(nums, mid) >= (total_subarrays + 1) // 2:
                high = mid
            else:
                low = mid + 1
        return low

# Example usage:
# sol = Solution()
# print(sol.medianOfUniquenessArray([1, 2, 3]))  # Output: 1
# print(sol.medianOfUniquenessArray([3, 4, 3, 4, 5]))  # Output: 2
# print(sol.medianOfUniquenessArray([4, 3, 5, 4]))  # Output: 2

def medianOfUniquenessArray(nums: List[int]) -> int:
    return Solution().medianOfUniquenessArray(nums)