import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        cs = sorted(s)
        n = len(cs)
        m = n // 2
        
        # Check if the middle elements are the same
        if cs[m] == cs[m - 1]:
            i = m
            # Find the first character after the middle that is different from cs[m-1]
            while i < n and cs[i] == cs[m - 1]:
                i += 1
            j = m
            # Try to swap with the second half to avoid making it a palindrome
            while j < n and cs[j] == cs[n - j - 1]:
                if i >= n:
                    return "-1"
                cs[i], cs[j] = cs[j], cs[i]
                i, j = i + 1, j + 1
        
        # Ensure the string is lexicographically smallest anti-palindrome
        for i in range(m):
            if cs[i] == cs[n - i - 1]:
                # Find a character to swap
                for k in range(i + 1, m):
                    if cs[k] != cs[n - i - 1]:
                        cs[i], cs[k] = cs[k], cs[i]
                        break
                else:
                    return "-1"
        
        return "".join(cs)

def makeAntiPalindrome(s: str) -> str:
    return Solution().makeAntiPalindrome(s)