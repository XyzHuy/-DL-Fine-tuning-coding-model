import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both the seats and students arrays
        seats.sort()
        students.sort()
        
        # Calculate the total number of moves required
        total_moves = sum(abs(seats[i] - students[i]) for i in range(len(seats)))
        
        return total_moves

def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    return Solution().minMovesToSeat(seats, students)