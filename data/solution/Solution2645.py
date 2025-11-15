import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def addMinimum(self, word: str) -> int:
        # Initialize the number of insertions needed
        insertions = 0
        # Initialize the expected character in the sequence "abc"
        expected = 'a'
        
        # Iterate over each character in the word
        for char in word:
            # While the current character does not match the expected character
            while char != expected:
                # Increment the insertions count
                insertions += 1
                # Move to the next expected character in the sequence "abc"
                expected = chr((ord(expected) - ord('a') + 1) % 3 + ord('a'))
            
            # Move to the next expected character in the sequence "abc"
            expected = chr((ord(expected) - ord('a') + 1) % 3 + ord('a'))
        
        # After the loop, count the remaining characters needed to complete the last "abc"
        while expected != 'a':
            insertions += 1
            expected = chr((ord(expected) - ord('a') + 1) % 3 + ord('a'))
        
        return insertions

def addMinimum(word: str) -> int:
    return Solution().addMinimum(word)