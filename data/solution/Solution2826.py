import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Initialize dp array with large numbers
        dp = [0, 0, 0]
        
        for num in nums:
            # Update dp for each possible last element in the non-decreasing sequence
            new_dp = [0] * 3
            new_dp[0] = dp[0] + (num != 1)
            new_dp[1] = min(dp[0], dp[1]) + (num != 2)
            new_dp[2] = min(dp[0], dp[1], dp[2]) + (num != 3)
            dp = new_dp
        
        # The result is the minimum value in the dp array
        return min(dp)

# Example usage:
# sol = Solution()
# print(sol.minimumOperations([2,1,3,2,1]))  # Output: 3
# print(sol.minimumOperations([1,3,2,1,3,3]))  # Output: 2
# print(sol.minimumOperations([2,2,2,2,3,3]))  # Output: 0

def minimumOperations(nums: List[int]) -> int:
    return Solution().minimumOperations(nums)