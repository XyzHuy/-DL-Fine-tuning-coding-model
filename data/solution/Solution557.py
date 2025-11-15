import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()
        # Reverse each word and join them back with a space
        reversed_words = ' '.join(word[::-1] for word in words)
        return reversed_words

def reverseWords(s: str) -> str:
    return Solution().reverseWords(s)