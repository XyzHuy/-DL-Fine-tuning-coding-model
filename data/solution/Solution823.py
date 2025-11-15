import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {num: 1 for num in arr}  # Each number can form a tree by itself
        
        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0:  # arr[j] is a factor of num
                    right_child = num // arr[j]
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[arr[j]] * dp[right_child]) % MOD
        
        return sum(dp.values()) % MOD

def numFactoredBinaryTrees(arr: List[int]) -> int:
    return Solution().numFactoredBinaryTrees(arr)