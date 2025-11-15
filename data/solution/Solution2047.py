import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid_word(word):
            hyphen_count = word.count('-')
            punctuation_count = sum(1 for char in word if char in '!.,')

            # Check for digits
            if any(char.isdigit() for char in word):
                return False
            
            # Check hyphen rules
            if hyphen_count > 1:
                return False
            if hyphen_count == 1:
                hyphen_index = word.index('-')
                if hyphen_index == 0 or hyphen_index == len(word) - 1:
                    return False
                if not (word[hyphen_index - 1].isalpha() and word[hyphen_index + 1].isalpha()):
                    return False
            
            # Check punctuation rules
            if punctuation_count > 1:
                return False
            if punctuation_count == 1 and not word.endswith(('!', '.', ',')):
                return False
            
            return True

        tokens = sentence.split()
        return sum(is_valid_word(token) for token in tokens)

def countValidWords(sentence: str) -> int:
    return Solution().countValidWords(sentence)