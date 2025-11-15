import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0
        for i in range(len(s)):
            # Odd length palindromes
            total_palindromes += expand_around_center(i, i)
            # Even length palindromes
            total_palindromes += expand_around_center(i, i + 1)

        return total_palindromes

def countSubstrings(s: str) -> int:
    return Solution().countSubstrings(s)