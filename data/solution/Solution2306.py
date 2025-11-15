import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Create a set for fast lookup
        ideas_set = set(ideas)
        
        # Initialize a 2D array to count valid swaps
        # swap_count[a][b] will count how many suffixes of words starting with 'a'
        # can be swapped with prefixes of words starting with 'b' to form valid names
        swap_count = [[0] * 26 for _ in range(26)]
        
        # Iterate over each idea
        for idea in ideas:
            # Get the first character and the suffix of the idea
            first_char = ord(idea[0]) - ord('a')
            suffix = idea[1:]
            
            # Try swapping the first character with every other character
            for other_char in range(26):
                # Form the new word with the swapped first character
                new_word = chr(other_char + ord('a')) + suffix
                
                # If the new word is not in the original set, it's a valid swap
                if new_word not in ideas_set:
                    swap_count[first_char][other_char] += 1
        
        # Calculate the total number of valid names
        total_valid_names = 0
        for i in range(26):
            for j in range(26):
                # Each valid swap (i, j) can form two distinct names: (i, j) and (j, i)
                total_valid_names += swap_count[i][j] * swap_count[j][i]
        
        return total_valid_names

def distinctNames(ideas: List[str]) -> int:
    return Solution().distinctNames(ideas)