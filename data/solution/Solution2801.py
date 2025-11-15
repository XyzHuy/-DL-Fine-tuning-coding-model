import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7
        
        def count_up_to(num_str):
            n = len(num_str)
            
            @lru_cache(None)
            def dp(i, is_limit, is_zero, prev_digit):
                if i == n:
                    return 1 if not is_zero else 0
                
                count = 0
                if is_zero:
                    count = dp(i + 1, False, True, -1)
                
                limit_digit = int(num_str[i]) if is_limit else 9
                
                for digit in range(10):
                    if is_zero and digit == 0:
                        continue
                    if is_limit and digit > limit_digit:
                        break
                    if is_zero or abs(prev_digit - digit) == 1:
                        count += dp(i + 1, is_limit and digit == limit_digit, False, digit)
                        count %= MOD
                
                return count
            
            return dp(0, True, True, -1)
        
        return (count_up_to(high) - count_up_to(str(int(low) - 1))) % MOD

def countSteppingNumbers(low: str, high: str) -> int:
    return Solution().countSteppingNumbers(low, high)