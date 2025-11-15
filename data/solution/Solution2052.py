import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        words = sentence.split()
        n = len(words)
        
        # dp[i] will store the minimum cost to split the first i words
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No cost for 0 words
        
        for i in range(1, n + 1):
            length = 0
            for j in range(i, 0, -1):
                # Add the length of the current word and a space if not the first word in the row
                length += len(words[j - 1]) + (1 if i - j > 0 else 0)
                if length <= k:
                    # Calculate the cost for this row and add it to the cost of the previous rows
                    cost = (k - length) ** 2 if i < n else 0
                    dp[i] = min(dp[i], dp[j - 1] + cost)
                else:
                    break
        
        return dp[n]

def minimumCost(sentence: str, k: int) -> int:
    return Solution().minimumCost(sentence, k)