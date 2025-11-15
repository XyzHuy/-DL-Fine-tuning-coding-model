import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # Create a dictionary to store the index of each character in string s
        index_map = {char: idx for idx, char in enumerate(s)}
        
        # Initialize the permutation difference
        permutation_difference = 0
        
        # Calculate the permutation difference by comparing indices in s and t
        for idx, char in enumerate(t):
            permutation_difference += abs(idx - index_map[char])
        
        return permutation_difference

def findPermutationDifference(s: str, t: str) -> int:
    return Solution().findPermutationDifference(s, t)