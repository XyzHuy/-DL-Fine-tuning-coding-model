import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            if num in (2, 3):
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        def is_palindrome(num):
            return str(num) == str(num)[::-1]

        # Special case for n in the range [8, 11]
        if 8 <= n <= 11:
            return 11

        # Generate odd-length palindromes
        length = len(str(n))
        while True:
            # Generate palindromes of the current length
            for half in range(10**(length // 2), 10**(length // 2 + 1)):
                # Create a palindrome
                if length % 2 == 0:
                    palindrome = int(str(half) + str(half)[::-1])
                else:
                    palindrome = int(str(half) + str(half)[-2::-1])
                
                if palindrome >= n and is_prime(palindrome):
                    return palindrome
            
            # Move to the next length
            length += 1

def primePalindrome(n: int) -> int:
    return Solution().primePalindrome(n)