import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        
        def count_up_to(num, min_sum, max_sum):
            n = len(num)
            dp = [[[-1] * (n + 1) for _ in range(max_sum + 1)] for _ in range(2)]
            
            def dfs(pos, tight, sum_digits):
                if sum_digits > max_sum:
                    return 0
                if pos == n:
                    return 1 if min_sum <= sum_digits <= max_sum else 0
                if dp[tight][sum_digits][pos] != -1:
                    return dp[tight][sum_digits][pos]
                
                limit = int(num[pos]) if tight else 9
                count = 0
                for d in range(limit + 1):
                    new_tight = tight and d == limit
                    count = (count + dfs(pos + 1, new_tight, sum_digits + d)) % MOD
                
                dp[tight][sum_digits][pos] = count
                return count
            
            return dfs(0, 1, 0)
        
        count2 = count_up_to(num2, min_sum, max_sum)
        count1_minus_1 = count_up_to(str(int(num1) - 1), min_sum, max_sum) if int(num1) > 0 else 0
        
        return (count2 - count1_minus_1 + MOD) % MOD

def count(num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    return Solution().count(num1, num2, min_sum, max_sum)