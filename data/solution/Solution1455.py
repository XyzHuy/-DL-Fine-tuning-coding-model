import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate over the words with their indices
        for index, word in enumerate(words):
            # Check if the current word starts with the searchWord
            if word.startswith(searchWord):
                # Return the 1-indexed position
                return index + 1
        
        # If no word is found, return -1
        return -1

def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    return Solution().isPrefixOfWord(sentence, searchWord)