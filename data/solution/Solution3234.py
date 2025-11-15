import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        total_substrings = n * (n + 1) // 2
        non_dominant_count = 0

        # Function to count zeros in a substring
        def count_zeros(sub):
            return sub.count('0')

        # Function to count ones in a substring
        def count_ones(sub):
            return sub.count('1')

        # Check all substrings
        for i in range(n):
            zeros = 0
            ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    zeros += 1
                else:
                    ones += 1
                if ones < zeros * zeros:
                    non_dominant_count += 1

        return total_substrings - non_dominant_count

# Example usage:
# sol = Solution()
# print(sol.numberOfSubstrings("00011"))  # Output: 5
# print(sol.numberOfSubstrings("101101")) # Output: 16

def numberOfSubstrings(s: str) -> int:
    return Solution().numberOfSubstrings(s)