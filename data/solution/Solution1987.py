import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7
        n = len(binary)
        
        # Initialize counts for subsequences ending with '0' and '1'
        end_with_0 = 0
        end_with_1 = 0
        
        # Check if there is at least one '0' in the binary string
        has_zero = '0' in binary
        
        for bit in binary:
            if bit == '0':
                # New subsequences ending with '0' can be formed by appending '0' to all existing subsequences
                end_with_0 = (end_with_0 + end_with_1) % MOD
            else:
                # New subsequences ending with '1' can be formed by appending '1' to all existing subsequences
                # plus the new subsequence which is the single '1' itself
                end_with_1 = (end_with_0 + end_with_1 + 1) % MOD
        
        # The total number of unique good subsequences is the sum of subsequences ending with '0' and '1'
        # If there is at least one '0', we need to add it to the result
        return (end_with_0 + end_with_1 + has_zero) % MOD

def numberOfUniqueGoodSubsequences(binary: str) -> int:
    return Solution().numberOfUniqueGoodSubsequences(binary)