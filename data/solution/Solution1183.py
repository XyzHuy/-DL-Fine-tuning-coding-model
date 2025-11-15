import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        from collections import Counter
        
        # Calculate the frequency of each cell position in the top-left sideLength x sideLength sub-matrix
        freq = Counter()
        for i in range(sideLength):
            for j in range(sideLength):
                # Count how many times the cell (i, j) appears in the matrix
                count_i = (height - i + sideLength - 1) // sideLength
                count_j = (width - j + sideLength - 1) // sideLength
                freq[(i, j)] = count_i * count_j
        
        # Sort the frequencies in descending order
        sorted_freq = sorted(freq.values(), reverse=True)
        
        # Sum the top maxOnes frequencies
        return sum(sorted_freq[:maxOnes])

def maximumNumberOfOnes(width: int, height: int, sideLength: int, maxOnes: int) -> int:
    return Solution().maximumNumberOfOnes(width, height, sideLength, maxOnes)