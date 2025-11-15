import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Extract all the letters from the string and reverse them
        letters = [c for c in s if c.isalpha()]
        letters.reverse()
        
        # Create a list from the original string to allow modification
        result = list(s)
        
        # Replace the letters in the result list with the reversed letters
        letter_index = 0
        for i in range(len(result)):
            if result[i].isalpha():
                result[i] = letters[letter_index]
                letter_index += 1
        
        # Join the list back into a string and return it
        return ''.join(result)

def reverseOnlyLetters(s: str) -> str:
    return Solution().reverseOnlyLetters(s)