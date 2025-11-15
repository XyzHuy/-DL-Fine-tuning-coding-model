import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize counters for open and close parentheses needed
        open_needed = 0
        close_needed = 0
        
        # Iterate through each character in the string
        for char in s:
            if char == '(':
                # If we encounter an open parenthesis, we might need a close one later
                open_needed += 1
            elif char == ')':
                if open_needed > 0:
                    # If we have an open parenthesis needed, this close one matches it
                    open_needed -= 1
                else:
                    # If no open parenthesis needed, this close one is unmatched
                    close_needed += 1
        
        # The total number of insertions needed is the sum of unmatched open and close parentheses
        return open_needed + close_needed

def minAddToMakeValid(s: str) -> int:
    return Solution().minAddToMakeValid(s)