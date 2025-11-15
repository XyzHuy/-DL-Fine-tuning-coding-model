import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        max_length = 0
        current_length = 0
        current_vowel_index = 0
        seen_all_vowels = False

        for i, char in enumerate(word):
            if char == vowels[current_vowel_index]:
                current_length += 1
                if current_vowel_index == 4:
                    seen_all_vowels = True
            elif current_vowel_index < 4 and char == vowels[current_vowel_index + 1]:
                current_vowel_index += 1
                current_length += 1
                if current_vowel_index == 4:
                    seen_all_vowels = True
            else:
                if seen_all_vowels:
                    max_length = max(max_length, current_length)
                if char == 'a':
                    current_length = 1
                    current_vowel_index = 0
                    seen_all_vowels = False
                else:
                    current_length = 0
                    current_vowel_index = 0
                    seen_all_vowels = False

        if seen_all_vowels:
            max_length = max(max_length, current_length)

        return max_length

def longestBeautifulSubstring(word: str) -> int:
    return Solution().longestBeautifulSubstring(word)