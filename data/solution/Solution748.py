import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Extract and count the letters in licensePlate, ignoring case and non-letter characters
        license_counter = Counter(char.lower() for char in licensePlate if char.isalpha())
        
        # Initialize the shortest completing word with a large length
        shortest_word = None
        
        # Iterate over each word in words
        for word in words:
            # Count the letters in the current word
            word_counter = Counter(word)
            
            # Check if the current word contains all the letters in licensePlate with at least the same frequency
            if all(word_counter[char] >= license_counter[char] for char in license_counter):
                # If it is the first valid word or shorter than the current shortest, update shortest_word
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word

def shortestCompletingWord(licensePlate: str, words: List[str]) -> str:
    return Solution().shortestCompletingWord(licensePlate, words)