import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Dictionary to store the length of the longest subsequence ending with a particular number
        dp = {}
        
        for num in arr:
            # If (num - difference) exists in dp, it means we can extend the subsequence ending at (num - difference)
            # Otherwise, start a new subsequence with the current number
            dp[num] = dp.get(num - difference, 0) + 1
        
        # The result is the maximum value in the dp dictionary, which represents the length of the longest subsequence
        return max(dp.values())

def longestSubsequence(arr: List[int], difference: int) -> int:
    return Solution().longestSubsequence(arr, difference)