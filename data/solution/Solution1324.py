import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        # Split the input string into words
        words = s.split()
        # Find the length of the longest word
        max_length = max(len(word) for word in words)
        # Initialize the result list with empty strings for each column
        result = [''] * max_length
        
        # Iterate over each position up to the length of the longest word
        for i in range(max_length):
            # Build each vertical word by iterating over each original word
            for word in words:
                # If the current word is long enough, add its character to the current column
                if i < len(word):
                    result[i] += word[i]
                else:
                    # Otherwise, add a space to maintain alignment
                    result[i] += ' '
        
        # Strip trailing spaces from each vertical word
        result = [word.rstrip() for word in result]
        
        return result

def printVertically(s: str) -> List[str]:
    return Solution().printVertically(s)