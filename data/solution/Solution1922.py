import collections
import string
import math
import datetime


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Number of even and odd indices
        even_count = (n + 1) // 2
        odd_count = n // 2
        
        # Function to perform modular exponentiation
        def power(base, exp, mod):
            result = 1
            base = base % mod
            while exp > 0:
                if (exp % 2) == 1:  # If exp is odd, multiply base with result
                    result = (result * base) % mod
                exp = exp >> 1  # Divide exp by 2
                base = (base * base) % mod  # Square the base
            return result
        
        # Calculate 5^even_count % MOD and 4^odd_count % MOD
        even_part = power(5, even_count, MOD)
        odd_part = power(4, odd_count, MOD)
        
        # Final result is (even_part * odd_part) % MOD
        return (even_part * odd_part) % MOD

def countGoodNumbers(n: int) -> int:
    return Solution().countGoodNumbers(n)