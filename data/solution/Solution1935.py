import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Convert the brokenLetters into a set for O(1) look-up time
        broken_set = set(brokenLetters)
        
        # Split the text into words
        words = text.split()
        
        # Initialize a counter for words that can be typed
        typed_words_count = 0
        
        # Iterate over each word in the text
        for word in words:
            # Check if any broken letter is in the current word
            if not any(letter in broken_set for letter in word):
                # If no broken letter is found, increment the counter
                typed_words_count += 1
        
        return typed_words_count

def canBeTypedWords(text: str, brokenLetters: str) -> int:
    return Solution().canBeTypedWords(text, brokenLetters)