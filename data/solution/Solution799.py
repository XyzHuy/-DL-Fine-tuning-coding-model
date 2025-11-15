import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize the first row with the poured champagne
        current_row = [poured]
        
        # Iterate through each row up to the query_row
        for row_num in range(1, query_row + 1):
            # Initialize the next row with zeros
            next_row = [0] * (row_num + 1)
            
            # Calculate the amount of champagne in each glass of the current row
            for i in range(len(current_row)):
                # If the current glass has more than 1 cup of champagne
                if current_row[i] > 1:
                    # Calculate the excess champagne
                    excess = (current_row[i] - 1) / 2
                    # Distribute the excess to the left and right glasses in the next row
                    next_row[i] += excess
                    next_row[i + 1] += excess
            
            # Move to the next row
            current_row = next_row
        
        # The amount of champagne in the queried glass cannot exceed 1
        return min(current_row[query_glass], 1)

def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    return Solution().champagneTower(poured, query_row, query_glass)