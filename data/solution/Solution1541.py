import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        balance = 0
        
        i = 0
        while i < len(s):
            if s[i] == '(':
                balance += 1
            else:
                # We found a ')'
                if balance > 0:
                    balance -= 1
                else:
                    # Need to insert a '(' to match this ')'
                    insertions += 1
                
                # Check for the second ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1  # Move past the second ')'
                else:
                    # Need to insert a ')' to make it '))'
                    insertions += 1
            
            i += 1
        
        # Each remaining '(' needs two ')' to be balanced
        insertions += 2 * balance
        
        return insertions

def minInsertions(s: str) -> int:
    return Solution().minInsertions(s)