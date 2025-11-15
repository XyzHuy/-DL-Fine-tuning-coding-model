import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        
        # KMP preprocessing to get the longest proper prefix which is also a suffix
        def compute_lps(evil):
            m = len(evil)
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if evil[i] == evil[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        lps = compute_lps(evil)
        m = len(evil)
        
        @cache
        def dp(pos, is_limit_lo, is_limit_hi, match_len):
            if match_len == m:
                return 0
            if pos == n:
                return 1
            
            lo = ord('a') if not is_limit_lo else ord(s1[pos])
            hi = ord('z') if not is_limit_hi else ord(s2[pos])
            count = 0
            
            for c in range(lo, hi + 1):
                char = chr(c)
                new_match_len = match_len
                while new_match_len > 0 and char != evil[new_match_len]:
                    new_match_len = lps[new_match_len - 1]
                if char == evil[new_match_len]:
                    new_match_len += 1
                
                new_is_limit_lo = is_limit_lo and char == s1[pos]
                new_is_limit_hi = is_limit_hi and char == s2[pos]
                
                count += dp(pos + 1, new_is_limit_lo, new_is_limit_hi, new_match_len)
                count %= MOD
            
            return count
        
        return dp(0, True, True, 0)

def findGoodStrings(n: int, s1: str, s2: str, evil: str) -> int:
    return Solution().findGoodStrings(n, s1, s2, evil)