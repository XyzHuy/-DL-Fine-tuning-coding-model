import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # Define the order of characters in "croak"
        order = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        # Initialize counters for each character in "croak"
        count = [0] * 5
        # Variable to keep track of the maximum number of frogs croaking simultaneously
        max_frogs = 0
        
        for char in croakOfFrogs:
            # Increment the count for the current character
            count[order[char]] += 1
            
            # Check if the sequence is valid
            for i in range(1, 5):
                if count[i] > count[i - 1]:
                    return -1
            
            # Update the maximum number of frogs croaking simultaneously
            max_frogs = max(max_frogs, count[0])
            
            # If a frog finishes croaking, decrement the count for all characters
            if char == 'k':
                for i in range(5):
                    count[i] -= 1
        
        # Check if all frogs have finished croaking
        if any(count):
            return -1
        
        return max_frogs

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    return Solution().minNumberOfFrogs(croakOfFrogs)