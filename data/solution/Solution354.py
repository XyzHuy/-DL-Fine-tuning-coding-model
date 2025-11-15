import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort the envelopes by width in ascending order and by height in descending order
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract the heights into a separate list
        heights = [envelope[1] for envelope in envelopes]
        
        # Initialize the dp array where dp[i] is the length of the LIS ending at index i
        dp = [1] * len(heights)
        
        # Fill the dp array
        for i in range(1, len(heights)):
            for j in range(i):
                if heights[j] < heights[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The result is the maximum value in the dp array
        return max(dp)

def maxEnvelopes(envelopes: List[List[int]]) -> int:
    return Solution().maxEnvelopes(envelopes)