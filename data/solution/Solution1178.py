import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # Function to convert a word to a bitmask
        def word_to_mask(word):
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            return mask
        
        # Count the frequency of each word's bitmask
        word_count = Counter(word_to_mask(word) for word in words)
        
        result = []
        
        # Process each puzzle
        for puzzle in puzzles:
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            puzzle_mask = word_to_mask(puzzle)
            count = 0
            
            # Generate all subsets of the puzzle bitmask
            sub_mask = puzzle_mask
            while sub_mask:
                # Only consider subsets that include the first character
                if sub_mask & first_char_mask:
                    count += word_count[sub_mask]
                # Move to the next subset
                sub_mask = (sub_mask - 1) & puzzle_mask
            
            # Include the empty subset case (though it will not be counted if it doesn't include the first character)
            result.append(count)
        
        return result

def findNumOfValidWords(words: List[str], puzzles: List[str]) -> List[int]:
    return Solution().findNumOfValidWords(words, puzzles)