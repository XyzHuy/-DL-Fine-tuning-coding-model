import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Initialize a list to store the number of ways to form strings of length i ending with each vowel
        # dp[i][j] will be the number of strings of length i ending with the j-th vowel
        dp = [[0] * 5 for _ in range(n + 1)]
        
        # Base case: There's one way to form a string of length 1 with each vowel
        for j in range(5):
            dp[1][j] = 1
        
        # Fill the dp table
        for i in range(2, n + 1):
            for j in range(5):
                # Sum up all the ways to form strings of length i-1 that end with a vowel <= current vowel
                dp[i][j] = sum(dp[i - 1][:j + 1])
        
        # The result is the sum of all ways to form strings of length n ending with any vowel
        return sum(dp[n])

# Example usage:
# sol = Solution()
# print(sol.countVowelStrings(1))  # Output: 5
# print(sol.countVowelStrings(2))  # Output: 15
# print(sol.countVowelStrings(33)) # Output: 66045

def countVowelStrings(n: int) -> int:
    return Solution().countVowelStrings(n)