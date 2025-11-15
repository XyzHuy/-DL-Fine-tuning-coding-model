import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            # Find the index of the first occurrence of ch
            index = word.index(ch)
            # Reverse the segment from the start to the index (inclusive) and concatenate with the rest of the string
            return word[:index+1][::-1] + word[index+1:]
        except ValueError:
            # If ch is not found, return the original word
            return word

def reversePrefix(word: str, ch: str) -> str:
    return Solution().reversePrefix(word, ch)