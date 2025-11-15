import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        # Calculate the upper and lower bounds for n-digit numbers
        upper_bound = 10**n - 1
        lower_bound = 10**(n-1)
        
        # Start from the largest possible number and go downwards
        for num1 in range(upper_bound, lower_bound - 1, -1):
            # Form the potential palindrome
            palindrome = int(str(num1) + str(num1)[::-1])
            
            # Check if the palindrome can be formed by the product of two n-digit numbers
            for num2 in range(upper_bound, lower_bound - 1, -1):
                if palindrome // num2 > upper_bound:
                    break  # Since num2 is decreasing, no need to check further
                if palindrome % num2 == 0:
                    return palindrome % 1337
        
        return 0  # This line should never be reached given the problem constraints

def largestPalindrome(n: int) -> int:
    return Solution().largestPalindrome(n)