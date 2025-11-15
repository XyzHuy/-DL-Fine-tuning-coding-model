import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half = num[:n // 2]
        
        # Convert the string to a list of characters for easier manipulation
        half_list = list(half)
        
        # Find the next lexicographical permutation of the first half
        k = -1
        for i in range(len(half_list) - 2, -1, -1):
            if half_list[i] < half_list[i + 1]:
                k = i
                break
        
        if k == -1:
            # No next permutation exists
            return ""
        
        # Find the smallest character larger than half_list[k] to the right of k
        l = -1
        for i in range(len(half_list) - 1, k, -1):
            if half_list[i] > half_list[k]:
                l = i
                break
        
        # Swap the characters at positions k and l
        half_list[k], half_list[l] = half_list[l], half_list[k]
        
        # Reverse the sequence to the right of k
        half_list = half_list[:k + 1] + half_list[k + 1:][::-1]
        
        # Form the new half
        new_half = ''.join(half_list)
        
        # Form the full palindrome
        if n % 2 == 0:
            return new_half + new_half[::-1]
        else:
            return new_half + num[n // 2] + new_half[::-1]

def nextPalindrome(num: str) -> str:
    return Solution().nextPalindrome(num)