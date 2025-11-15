import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def arrangeWords(self, text: str) -> str:
        # Split the text into words
        words = text.split()
        
        # Convert the first word to lowercase for uniform sorting
        words[0] = words[0].lower()
        
        # Sort the words by their length, maintaining original order for ties
        sorted_words = sorted(words, key=len)
        
        # Capitalize the first word of the sorted list
        sorted_words[0] = sorted_words[0].capitalize()
        
        # Join the sorted words back into a single string
        return ' '.join(sorted_words)

def arrangeWords(text: str) -> str:
    return Solution().arrangeWords(text)