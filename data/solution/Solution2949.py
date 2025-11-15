import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        prefix_vowels = [0] * (n + 1)
        
        # Create a prefix sum array for vowels
        for i in range(n):
            prefix_vowels[i + 1] = prefix_vowels[i] + (s[i] in vowels_set)
        
        beautiful_count = 0
        
        # Check all possible substrings
        for i in range(n):
            for j in range(i + 1, n + 1):
                vowels = prefix_vowels[j] - prefix_vowels[i]
                consonants = (j - i) - vowels
                if vowels == consonants and (vowels * consonants) % k == 0:
                    beautiful_count += 1
        
        return beautiful_count

def beautifulSubstrings(s: str, k: int) -> int:
    return Solution().beautifulSubstrings(s, k)