import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If the lengths of s1 and s2 don't add up to the length of s3, return False
        if len(s1) + len(s2) != len(s3):
            return False

        # Use dynamic programming to solve this problem
        # dp[j] will be True if s3[0:j+i] can be formed by interleaving s1[0:i] and s2[0:j]
        dp = [False] * (len(s2) + 1)
        dp[0] = True  # Base case: both s1 and s2 are empty, s3 is empty

        # Fill the dp array for the case when s1 is empty
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the dp array for the rest of the cases
        for i in range(1, len(s1) + 1):
            # Update dp[0] for the case when s2 is empty
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                # Update dp[j] by considering two possibilities:
                # 1. The last character of s3 is from s1
                # 2. The last character of s3 is from s2
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[len(s2)]

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    return Solution().isInterleave(s1, s2, s3)