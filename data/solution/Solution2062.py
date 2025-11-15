import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0
        n = len(word)
        
        for i in range(n - 4):  # Start from the first possible starting point of a substring of length 5
            if word[i] in vowels:  # Only start if the character is a vowel
                seen_vowels = set()
                for j in range(i, n):
                    if word[j] in vowels:
                        seen_vowels.add(word[j])
                        if len(seen_vowels) == 5:  # All five vowels are present
                            count += 1
                    else:
                        break  # No need to continue if a non-vowel is found
        
        return count

def countVowelSubstrings(word: str) -> int:
    return Solution().countVowelSubstrings(word)