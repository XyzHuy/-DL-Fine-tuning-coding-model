import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Function to get the next character cyclically
        def next_char(c):
            return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        
        # Pointers for str1 and str2
        i, j = 0, 0
        
        # Iterate through str1
        while i < len(str1) and j < len(str2):
            # Check if characters match or if str1's character can be incremented to match str2's character
            if str1[i] == str2[j] or next_char(str1[i]) == str2[j]:
                j += 1  # Move to the next character in str2
            i += 1  # Move to the next character in str1
        
        # If we have traversed all characters in str2, it is a subsequence of str1
        return j == len(str2)

def canMakeSubsequence(str1: str, str2: str) -> bool:
    return Solution().canMakeSubsequence(str1, str2)