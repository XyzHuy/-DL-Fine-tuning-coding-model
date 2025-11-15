import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Get the column letter and row number from the coordinates
        column = coordinates[0]
        row = int(coordinates[1])
        
        # Convert the column letter to a number (a=1, b=2, ..., h=8)
        column_number = ord(column) - ord('a') + 1
        
        # A square is white if the sum of the column number and row number is odd
        return (column_number + row) % 2 == 1

def squareIsWhite(coordinates: str) -> bool:
    return Solution().squareIsWhite(coordinates)