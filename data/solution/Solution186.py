import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Reverse the entire character array
        s.reverse()
        
        # Initialize pointers for reversing each word
        start = 0
        end = 0
        n = len(s)
        
        # Reverse each word in the reversed array
        while start < n:
            # Find the end of the current word
            while end < n and s[end] != ' ':
                end += 1
            
            # Reverse the current word
            s[start:end] = reversed(s[start:end])
            
            # Move to the next word
            start = end + 1
            end += 1

def reverseWords(s: List[str]) -> None:
    return Solution().reverseWords(s)