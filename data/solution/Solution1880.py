import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def letter_value(letter):
            return str(ord(letter) - ord('a'))
        
        def word_value(word):
            return int(''.join(letter_value(letter) for letter in word))
        
        first_value = word_value(firstWord)
        second_value = word_value(secondWord)
        target_value = word_value(targetWord)
        
        return first_value + second_value == target_value

def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    return Solution().isSumEqual(firstWord, secondWord, targetWord)