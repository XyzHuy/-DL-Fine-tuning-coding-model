import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowels = 0
        current_vowels = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in vowels:
                current_vowels += 1
            
            if right >= k:
                if s[left] in vowels:
                    current_vowels -= 1
                left += 1
            
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels

def maxVowels(s: str, k: int) -> int:
    return Solution().maxVowels(s, k)