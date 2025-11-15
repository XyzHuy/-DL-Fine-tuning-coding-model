import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Sort the satisfaction levels in descending order
        satisfaction.sort(reverse=True)
        
        max_sum = 0
        current_sum = 0
        
        # Iterate through the sorted satisfaction levels
        for s in satisfaction:
            # Add the current satisfaction level to the current sum
            current_sum += s
            # If the current sum is negative, we should stop adding more dishes
            if current_sum < 0:
                break
            # Add the current sum to the maximum sum
            max_sum += current_sum
        
        return max_sum

# Example usage:
# solution = Solution()
# print(solution.maxSatisfaction([-1,-8,0,5,-9]))  # Output: 14
# print(solution.maxSatisfaction([4,3,2]))         # Output: 20
# print(solution.maxSatisfaction([-1,-4,-5]))      # Output: 0

def maxSatisfaction(satisfaction: List[int]) -> int:
    return Solution().maxSatisfaction(satisfaction)