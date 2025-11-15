import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def and_all(lst):
            result = -1
            for num in lst:
                result &= num
            return result
        
        count = 0
        n = len(nums)
        
        # Iterate over each possible starting point of the subarray
        for start in range(n):
            current_and = -1  # Start with -1 which is all bits set in binary
            for end in range(start, n):
                current_and &= nums[end]
                if current_and == k:
                    count += 1
                # Since we are doing bitwise AND, if it becomes 0, it will never be k again
                elif current_and == 0:
                    break
        
        return count

# Example usage:
# solution = Solution()
# print(solution.countSubarrays([1,1,1], 1))  # Output: 6
# print(solution.countSubarrays([1,1,2], 1))  # Output: 3
# print(solution.countSubarrays([1,2,3], 2))  # Output: 2

def countSubarrays(nums: List[int], k: int) -> int:
    return Solution().countSubarrays(nums, k)