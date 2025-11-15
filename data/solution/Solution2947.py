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
        count = 0

        # Iterate over all possible starting points of substrings
        for i in range(n):
            vowels = 0
            consonants = 0
            
            # Iterate over all possible ending points of substrings starting from i
            for j in range(i, n):
                if s[j] in vowels_set:
                    vowels += 1
                else:
                    consonants += 1
                
                # Check if the current substring is beautiful
                if vowels == consonants and (vowels * consonants) % k == 0:
                    count += 1

        return count

def beautifulSubstrings(s: str, k: int) -> int:
    return Solution().beautifulSubstrings(s, k)