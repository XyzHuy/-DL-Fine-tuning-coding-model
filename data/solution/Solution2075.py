import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Calculate the number of columns
        cols = len(encodedText) // rows
        
        # Create a matrix to store the characters
        matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
        
        # Fill the matrix with characters from encodedText
        index = 0
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = encodedText[index]
                index += 1
        
        # Extract the original text by following the diagonal order
        originalText = []
        for c in range(cols):
            r, col = 0, c
            while r < rows and col < cols:
                originalText.append(matrix[r][col])
                r += 1
                col += 1
        
        # Join the characters and remove trailing spaces
        return ''.join(originalText).rstrip()

def decodeCiphertext(encodedText: str, rows: int) -> str:
    return Solution().decodeCiphertext(encodedText, rows)