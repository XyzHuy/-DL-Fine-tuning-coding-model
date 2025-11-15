import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Initialize an array to keep track of the changes in seat reservations
        seat_changes = [0] * (n + 1)
        
        # Process each booking
        for first, last, seats in bookings:
            # Add seats to the first flight of the booking range
            seat_changes[first - 1] += seats
            # Subtract seats from the flight right after the last flight of the booking range
            seat_changes[last] -= seats
        
        # Calculate the total seats reserved for each flight
        total_seats = [0] * n
        current_seats = 0
        for i in range(n):
            current_seats += seat_changes[i]
            total_seats[i] = current_seats
        
        return total_seats

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    return Solution().corpFlightBookings(bookings, n)