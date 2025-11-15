import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Dictionary to store the first and last occurrence of each character
        first_last_occurrence = {}
        
        # Populate the dictionary with the first and last occurrence of each character
        for i, char in enumerate(s):
            if char not in first_last_occurrence:
                first_last_occurrence[char] = [i, i]
            else:
                first_last_occurrence[char][1] = i
        
        unique_palindromes = set()
        
        # Check for unique palindromic subsequences of length 3
        for char, (first, last) in first_last_occurrence.items():
            if first < last:
                # Add all unique characters between the first and last occurrence of char
                unique_palindromes.update({char + mid_char + char for mid_char in s[first + 1:last]})
        
        return len(unique_palindromes)

def countPalindromicSubsequence(s: str) -> int:
    return Solution().countPalindromicSubsequence(s)