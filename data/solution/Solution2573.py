import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        # Initialize the string with -1 (indicating no character assigned yet)
        word = [-1] * n
        
        # Assign the smallest possible character to each position
        char = 0
        for i in range(n):
            if word[i] == -1:
                if char >= 26:
                    return ""  # More than 26 distinct characters needed
                word[i] = char
                char += 1
                # Assign the same character to all positions that should match
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = word[i]
        
        # Verify the lcp matrix
        for i in range(n):
            for j in range(n):
                if word[i] == word[j]:
                    # Calculate the actual lcp for word[i:] and word[j:]
                    length = 0
                    for k in range(min(n - i, n - j)):
                        if word[i + k] == word[j + k]:
                            length += 1
                        else:
                            break
                    if length != lcp[i][j]:
                        return ""
                else:
                    if lcp[i][j] != 0:
                        return ""
        
        # Convert the word list to a string
        return ''.join(chr(ord('a') + c) for c in word)

def findTheString(lcp: List[List[int]]) -> str:
    return Solution().findTheString(lcp)