import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the input text
        text_count = Counter(text)
        
        # Count the frequency of each character in the word "balloon"
        balloon_count = Counter("balloon")
        
        # Initialize the result to a large number
        result = float('inf')
        
        # For each character in "balloon", calculate how many times we can use it
        for char in balloon_count:
            if char in text_count:
                # We can use the character text_count[char] // balloon_count[char] times
                result = min(result, text_count[char] // balloon_count[char])
            else:
                # If the character is not in the text, we can't form "balloon"
                return 0
        
        return result

def maxNumberOfBalloons(text: str) -> int:
    return Solution().maxNumberOfBalloons(text)