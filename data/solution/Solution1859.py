import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sortSentence(self, s: str) -> str:
        # Split the shuffled sentence into words
        words = s.split()
        
        # Create a list to hold the words in their correct order
        ordered_words = [''] * len(words)
        
        # Iterate over each word in the shuffled sentence
        for word in words:
            # The last character of the word is the position
            position = int(word[-1]) - 1
            # The word without the position number
            ordered_words[position] = word[:-1]
        
        # Join the ordered words into a single string with spaces
        return ' '.join(ordered_words)

def sortSentence(s: str) -> str:
    return Solution().sortSentence(s)