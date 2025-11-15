import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Dictionary to store reserved seats for each row
        reserved_dict = {}
        
        for row, seat in reservedSeats:
            if row not in reserved_dict:
                reserved_dict[row] = set()
            reserved_dict[row].add(seat)
        
        # Possible seat configurations for a family
        seat_configurations = {
            'left': {2, 3, 4, 5},
            'middle': {4, 5, 6, 7},
            'right': {6, 7, 8, 9}
        }
        
        max_families = 0
        
        # Check each row with reserved seats
        for row, reserved in reserved_dict.items():
            # Check if both left and right can be occupied
            if seat_configurations['left'].isdisjoint(reserved) and seat_configurations['right'].isdisjoint(reserved):
                max_families += 2
            # Check if either left, middle, or right can be occupied
            elif seat_configurations['left'].isdisjoint(reserved) or seat_configurations['middle'].isdisjoint(reserved) or seat_configurations['right'].isdisjoint(reserved):
                max_families += 1
        
        # For rows without any reserved seats, we can place 2 families per row
        max_families += 2 * (n - len(reserved_dict))
        
        return max_families

def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:
    return Solution().maxNumberOfFamilies(n, reservedSeats)