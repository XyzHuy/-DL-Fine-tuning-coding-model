import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findIntegers(self, n: int) -> int:
        # Convert n to binary string and reverse it for easier processing
        bin_n = bin(n)[2:][::-1]
        length = len(bin_n)
        
        # dp[i] will store the count of valid numbers of length i
        dp = [0] * (length + 1)
        dp[0] = 1  # There's one valid number of length 0: ""
        dp[1] = 2  # There are two valid numbers of length 1: "0", "1"
        
        # Fill dp array
        for i in range(2, length + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        result = 0
        last_bit = 0
        
        for i in range(length - 1, -1, -1):
            if bin_n[i] == '1':
                result += dp[i]
                if last_bit == 1:
                    # If we have two consecutive ones, we cannot have any valid number beyond this point
                    result -= 1
                    break
            last_bit = int(bin_n[i])
        
        # Always include 0 in the count
        result += 1
        
        return result

def findIntegers(n: int) -> int:
    return Solution().findIntegers(n)