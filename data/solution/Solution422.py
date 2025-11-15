import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # Get the number of rows
        numRows = len(words)
        
        # Iterate over each row
        for r in range(numRows):
            # Get the word at the current row
            rowWord = words[r]
            
            # Iterate over each character in the row word
            for c in range(len(rowWord)):
                # Check if the column index is within the number of rows
                if c >= numRows:
                    return False
                
                # Get the word at the current column
                colWord = words[c]
                
                # Check if the row index is within the length of the column word
                if r >= len(colWord):
                    return False
                
                # Compare the characters at the current position in the row and column words
                if rowWord[c] != colWord[r]:
                    return False
        
        return True

def validWordSquare(words: List[str]) -> bool:
    return Solution().validWordSquare(words)