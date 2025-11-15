import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        num_set = set(nums)
        power_of_two = 1
        
        while True:
            if power_of_two not in num_set:
                return power_of_two
            power_of_two *= 2

# Example usage:
# sol = Solution()
# print(sol.minImpossibleOR([2, 1]))  # Output: 4
# print(sol.minImpossibleOR([5, 3, 2]))  # Output: 1

def minImpossibleOR(nums: List[int]) -> int:
    return Solution().minImpossibleOR(nums)