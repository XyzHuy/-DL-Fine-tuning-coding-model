import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set('aeiou')
        total_vowels = 0
        n = len(word)
        
        for i, char in enumerate(word):
            if char in vowels:
                # Calculate the number of substrings in which the current vowel is included
                total_vowels += (i + 1) * (n - i)
        
        return total_vowels

def countVowels(word: str) -> int:
    return Solution().countVowels(word)