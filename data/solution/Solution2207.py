import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b = pattern[0], pattern[1]
        
        # If both characters in the pattern are the same, we need a special approach
        if a == b:
            count_a = text.count(a)
            # If we add one more 'a', we can form count_a + 1 new pairs
            # The total number of subsequences is the sum of the first count_a numbers
            return (count_a + 1) * count_a // 2
        
        # Count occurrences of a and b in the text
        count_a = count_b = 0
        subsequences = 0
        
        for char in text:
            if char == b:
                # Each 'b' can pair with all previous 'a's
                subsequences += count_a
                count_b += 1
            elif char == a:
                count_a += 1
        
        # Option 1: Add 'a' at the beginning or anywhere
        # This adds count_b new subsequences (each 'b' can pair with the new 'a')
        option1 = subsequences + count_b
        
        # Option 2: Add 'b' at the end or anywhere
        # This adds count_a new subsequences (each 'a' can pair with the new 'b')
        option2 = subsequences + count_a
        
        return max(option1, option2)

def maximumSubsequenceCount(text: str, pattern: str) -> int:
    return Solution().maximumSubsequenceCount(text, pattern)