import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # Create a dictionary to map each character to its index on the keyboard
        index_map = {char: i for i, char in enumerate(keyboard)}
        
        # Initialize the total time with the position of the first character
        total_time = index_map[word[0]]
        
        # Calculate the time to move between consecutive characters
        for i in range(1, len(word)):
            total_time += abs(index_map[word[i]] - index_map[word[i - 1]])
        
        return total_time

def calculateTime(keyboard: str, word: str) -> int:
    return Solution().calculateTime(keyboard, word)