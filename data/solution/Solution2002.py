import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        pal_lengths = {}
        
        # Function to check if a subsequence represented by a bitmask is a palindrome
        def is_palindrome(mask):
            subseq = [s[i] for i in range(n) if (1 << i) & mask]
            return subseq == subseq[::-1]
        
        # Iterate through all possible subsequences
        for mask in range(1, 1 << n):
            if is_palindrome(mask):
                pal_lengths[mask] = bin(mask).count('1')
        
        max_product = 0
        
        # Check all pairs of disjoint palindromic subsequences
        for mask1 in pal_lengths:
            for mask2 in pal_lengths:
                if mask1 & mask2 == 0:  # Disjoint subsequences
                    max_product = max(max_product, pal_lengths[mask1] * pal_lengths[mask2])
        
        return max_product

def maxProduct(s: str) -> int:
    return Solution().maxProduct(s)