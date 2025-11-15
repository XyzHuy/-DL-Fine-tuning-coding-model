import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        
        # Convert the string to a list to allow modification
        pal_list = list(palindrome)
        
        # Try to change the first non-'a' character to 'a'
        for i in range(n // 2):
            if pal_list[i] != 'a':
                pal_list[i] = 'a'
                return ''.join(pal_list)
        
        # If all characters are 'a' or the string is odd and the middle character is the only one not changed
        # Change the last character to 'b'
        pal_list[-1] = 'b'
        return ''.join(pal_list)

def breakPalindrome(palindrome: str) -> str:
    return Solution().breakPalindrome(palindrome)