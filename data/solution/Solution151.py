import collections
import string
import math
import datetime


class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces and filter out any empty strings
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the words with a single space
        return ' '.join(words)

def reverseWords(s: str) -> str:
    return Solution().reverseWords(s)