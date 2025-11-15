import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        
        # Generate candidates
        # 1. The number with one less digit, all 9s
        candidate1 = '9' * (length - 1)
        
        # 2. The number with one more digit, 1 followed by length-1 zeros and ending with 1
        candidate2 = '1' + '0' * (length - 1) + '1'
        
        # 3. The palindrome closest to the original number
        prefix = n[:(length + 1) // 2]
        prefix_int = int(prefix)
        
        # Generate palindromes by manipulating the prefix
        for x in [prefix_int - 1, prefix_int, prefix_int + 1]:
            if length % 2 == 0:
                candidate = str(x) + str(x)[::-1]
            else:
                candidate = str(x) + str(x)[:-1][::-1]
            
            # Avoid the number itself
            if candidate != n:
                candidate2 = min(candidate2, candidate, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        # Compare the candidates
        return min(candidate1, candidate2, key=lambda x: (abs(int(x) - int(n)), int(x)))

def nearestPalindromic(n: str) -> str:
    return Solution().nearestPalindromic(n)