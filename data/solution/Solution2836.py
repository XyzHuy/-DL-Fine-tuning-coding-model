import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        
        # Number of bits required to represent k
        max_pow = k.bit_length()
        
        # dp[j][i] will store the (2^j)-th ancestor of i and the sum of indices encountered
        dp = [[(0, 0) for _ in range(n)] for _ in range(max_pow)]
        
        # Initialize dp[0][i] which is the 1st ancestor (receiver[i]) and the sum is i + receiver[i]
        for i in range(n):
            dp[0][i] = (receiver[i], i + receiver[i])
        
        # Fill the dp table for higher powers of 2
        for j in range(1, max_pow):
            for i in range(n):
                prev_node, prev_sum = dp[j-1][i]
                next_node, next_sum = dp[j-1][prev_node]
                dp[j][i] = (next_node, prev_sum + next_sum - prev_node)
        
        def get_kth_ancestor_and_sum(start, k):
            current_node = start
            current_sum = start
            j = 0
            while k > 0:
                if k & 1:
                    current_sum += dp[j][current_node][1] - current_node
                    current_node = dp[j][current_node][0]
                k >>= 1
                j += 1
            return current_sum
        
        # Find the maximum score starting from any node
        max_score = 0
        for i in range(n):
            max_score = max(max_score, get_kth_ancestor_and_sum(i, k))
        
        return max_score

def getMaxFunctionValue(receiver: List[int], k: int) -> int:
    return Solution().getMaxFunctionValue(receiver, k)