import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        # Extract vowels from the string and sort them
        sorted_vowels = sorted([char for char in s if char in vowels])
        
        # Iterator for the sorted vowels
        vowel_iter = iter(sorted_vowels)
        
        # Construct the result string
        result = ''.join(next(vowel_iter) if char in vowels else char for char in s)
        
        return result

def sortVowels(s: str) -> str:
    return Solution().sortVowels(s)