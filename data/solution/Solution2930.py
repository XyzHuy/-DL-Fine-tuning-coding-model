import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i][mask] will store the number of ways to form a string of length i with the given mask
        # mask is a 4-bit number where each bit represents if we have included 'e', 'e', 'l', 't'
        dp = [[0] * 16 for _ in range(n + 1)]
        dp[0][0] = 1  # base case: one way to form a string of length 0 with no characters included

        for i in range(1, n + 1):
            for mask in range(16):
                # Try adding each of the 26 characters
                for c in range(26):
                    new_mask = mask
                    if c == ord('e') - ord('a'):
                        # If we are adding 'e', we need to check if we already have one 'e'
                        if (mask & 1) == 0:
                            new_mask |= 1
                        elif (mask & 2) == 0:
                            new_mask |= 2
                    elif c == ord('l') - ord('a'):
                        if (mask & 4) == 0:
                            new_mask |= 4
                    elif c == ord('t') - ord('a'):
                        if (mask & 8) == 0:
                            new_mask |= 8
                    dp[i][new_mask] = (dp[i][new_mask] + dp[i - 1][mask]) % MOD

        # The final answer is the number of ways to form a string of length n with all bits set (i.e., 'e', 'e', 'l', 't' included)
        return dp[n][15]

# Example usage:
# sol = Solution()
# print(sol.stringCount(4))  # Output: 12
# print(sol.stringCount(10)) # Output: 83943898

def stringCount(n: int) -> int:
    return Solution().stringCount(n)