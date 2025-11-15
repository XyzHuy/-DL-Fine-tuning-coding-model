import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        
        # dp[i] will store the number of ways to decode the first i keys
        dp = [0] * (len(pressedKeys) + 1)
        dp[0] = 1  # There's one way to decode an empty string
        
        for i in range(1, len(pressedKeys) + 1):
            # The current key can always be a single press
            dp[i] = dp[i - 1]
            
            # Check for sequences of the same key
            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] = (dp[i] + dp[i - 2]) % MOD
                if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 3]:
                    dp[i] = (dp[i] + dp[i - 3]) % MOD
                    if i >= 4 and pressedKeys[i - 1] in '79' and pressedKeys[i - 1] == pressedKeys[i - 4]:
                        dp[i] = (dp[i] + dp[i - 4]) % MOD
        
        return dp[-1]

def countTexts(pressedKeys: str) -> int:
    return Solution().countTexts(pressedKeys)