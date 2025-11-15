import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        # Dictionary to store the first occurrence of each character in firstString
        first_occurrence = {}
        # Dictionary to store the last occurrence of each character in secondString
        last_occurrence = {}
        
        # Fill the first_occurrence dictionary
        for i, char in enumerate(firstString):
            if char not in first_occurrence:
                first_occurrence[char] = i
        
        # Fill the last_occurrence dictionary
        for i in range(len(secondString) - 1, -1, -1):
            char = secondString[i]
            if char not in last_occurrence:
                last_occurrence[char] = i
        
        # Initialize variables to track the minimum difference and the count of quadruples
        min_diff = float('inf')
        count = 0
        
        # Iterate over all characters that appear in both strings
        for char in first_occurrence:
            if char in last_occurrence:
                diff = first_occurrence[char] - last_occurrence[char]
                if diff < min_diff:
                    min_diff = diff
                    count = 1
                elif diff == min_diff:
                    count += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.countQuadruples("abcd", "bccda"))  # Output: 1
# print(sol.countQuadruples("ab", "cd"))      # Output: 0

def countQuadruples(firstString: str, secondString: str) -> int:
    return Solution().countQuadruples(firstString, secondString)