import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        current_time = 0
        
        for arrival, time_needed in customers:
            # Update the current time to the maximum of arrival time or when the chef is free
            current_time = max(current_time, arrival) + time_needed
            # Calculate the waiting time for the current customer
            waiting_time = current_time - arrival
            # Add the waiting time to the total
            total_waiting_time += waiting_time
        
        # Calculate the average waiting time
        average_waiting_time = total_waiting_time / len(customers)
        return average_waiting_time

def averageWaitingTime(customers: List[List[int]]) -> float:
    return Solution().averageWaitingTime(customers)