import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Initialize an array to keep track of the longest subsequence ending with each character
        dp = [0] * 26
        
        for char in s:
            # Convert character to index (0 for 'a', 1 for 'b', ..., 25 for 'z')
            index = ord(char) - ord('a')
            
            # Calculate the maximum length of the ideal subsequence ending with this character
            max_length = 1
            for offset in range(-k, k + 1):
                if 0 <= index + offset < 26:
                    max_length = max(max_length, dp[index + offset] + 1)
            
            # Update the dp array with the calculated maximum length
            dp[index] = max_length
        
        # The result is the maximum value in the dp array
        return max(dp)

def longestIdealString(s: str, k: int) -> int:
    return Solution().longestIdealString(s, k)