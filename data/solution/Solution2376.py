import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        from functools import lru_cache
        
        # Convert the number to a list of its digits
        digits = list(map(int, str(n)))
        length = len(digits)
        
        @lru_cache(None)
        def dp(pos: int, mask: int, is_tight: bool) -> int:
            # If we've processed all digits, check if we have used any digits (mask > 0)
            if pos == length:
                return mask > 0
            
            # Get the upper limit for the current digit
            limit = digits[pos] if is_tight else 9
            count = 0
            
            # Iterate over all possible digits
            for d in range(limit + 1):
                # If the digit is not used yet (not in the mask)
                if mask & (1 << d) == 0:
                    # If this is the first digit and it's 0, we skip it
                    if d == 0 and mask == 0:
                        count += dp(pos + 1, mask, False)
                    else:
                        # Recur for the next position
                        count += dp(pos + 1, mask | (1 << d), is_tight and d == limit)
            
            return count
        
        # Start the DP with the first position, mask 0 (no digits used), and is_tight True
        return dp(0, 0, True)

# Example usage:
# sol = Solution()
# print(sol.countSpecialNumbers(20))  # Output: 19
# print(sol.countSpecialNumbers(5))   # Output: 5
# print(sol.countSpecialNumbers(135)) # Output: 110

def countSpecialNumbers(n: int) -> int:
    return Solution().countSpecialNumbers(n)