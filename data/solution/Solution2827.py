import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count(n: int) -> int:
            n_str = str(n)
            m = len(n_str)
            
            @lru_cache(None)
            def dfs(pos: int, is_limit: bool, is_num: bool, balance: int, mod: int) -> int:
                if pos == m:
                    return int(is_num and balance == 0 and mod == 0)
                
                res = 0
                if not is_num:
                    res += dfs(pos + 1, False, False, balance, mod)
                
                up = int(n_str[pos]) if is_limit else 9
                for d in range(0 if is_num else 1, up + 1):
                    new_balance = balance + (1 if d % 2 == 0 else -1)
                    new_mod = (mod * 10 + d) % k
                    res += dfs(pos + 1, is_limit and d == up, True, new_balance, new_mod)
                
                return res
            
            return dfs(0, True, False, 0, 0)
        
        return count(high) - count(low - 1)

def numberOfBeautifulIntegers(low: int, high: int, k: int) -> int:
    return Solution().numberOfBeautifulIntegers(low, high, k)