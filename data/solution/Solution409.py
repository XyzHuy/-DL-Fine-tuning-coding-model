import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        
        # Initialize the length of the longest palindrome
        length = 0
        
        # Flag to check if we have added an odd count character in the middle
        odd_used = False
        
        # Iterate over the character counts
        for count in char_count.values():
            if count % 2 == 0:
                # If the count is even, we can add the whole count to the palindrome length
                length += count
            else:
                # If the count is odd, we can add count - 1 to the palindrome length
                length += count - 1
                # If we haven't used an odd count character in the middle yet, we can use one
                if not odd_used:
                    length += 1
                    odd_used = True
        
        return length

def longestPalindrome(s: str) -> int:
    return Solution().longestPalindrome(s)