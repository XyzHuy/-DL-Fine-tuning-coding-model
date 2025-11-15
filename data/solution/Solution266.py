import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # A string can form a palindrome if it has at most one character with an odd frequency
        return odd_count <= 1

def canPermutePalindrome(s: str) -> bool:
    return Solution().canPermutePalindrome(s)