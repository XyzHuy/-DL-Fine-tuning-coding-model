import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Morse code representations for each letter a-z
        morse_code = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        # Set to store unique transformations
        unique_transformations = set()
        
        # Iterate over each word in the list
        for word in words:
            # Convert the word to its Morse code transformation
            transformation = ''.join(morse_code[ord(char) - ord('a')] for char in word)
            # Add the transformation to the set
            unique_transformations.add(transformation)
        
        # Return the number of unique transformations
        return len(unique_transformations)

def uniqueMorseRepresentations(words: List[str]) -> int:
    return Solution().uniqueMorseRepresentations(words)