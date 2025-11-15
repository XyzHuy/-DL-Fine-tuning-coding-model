import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        # Convert the string to a list to allow modification
        s_list = list(s)
        left = 0
        right = len(s) - 1
        
        # Use two pointers to compare characters from both ends
        while left < right:
            # Replace the larger character with the smaller one
            if s_list[left] < s_list[right]:
                s_list[right] = s_list[left]
            elif s_list[left] > s_list[right]:
                s_list[left] = s_list[right]
            # Move the pointers towards the center
            left += 1
            right -= 1
        
        # Join the list back into a string and return
        return ''.join(s_list)

def makeSmallestPalindrome(s: str) -> str:
    return Solution().makeSmallestPalindrome(s)