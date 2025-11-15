import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestPrefix(self, s: str) -> str:
        def compute_prefix_function(s):
            n = len(s)
            pi = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            return pi
        
        n = len(s)
        pi = compute_prefix_function(s)
        longest_happy_prefix_length = pi[n - 1]
        return s[:longest_happy_prefix_length]

# Example usage:
# sol = Solution()
# print(sol.longestPrefix("level"))  # Output: "l"
# print(sol.longestPrefix("ababab"))  # Output: "abab"

def longestPrefix(s: str) -> str:
    return Solution().longestPrefix(s)