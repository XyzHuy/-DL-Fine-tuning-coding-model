import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maxScore(self, prices: List[int]) -> int:
        # Dictionary to store the sum of prices for each group
        group_sums = defaultdict(int)
        
        # Group indices by the value prices[i] - i
        for i, price in enumerate(prices):
            group_sums[price - i] += price
        
        # The maximum score is the maximum sum in any group
        return max(group_sums.values())

# Example usage:
# sol = Solution()
# print(sol.maxScore([1, 5, 3, 7, 8]))  # Output: 20
# print(sol.maxScore([5, 6, 7, 8, 9]))  # Output: 35

def maxScore(prices: List[int]) -> int:
    return Solution().maxScore(prices)