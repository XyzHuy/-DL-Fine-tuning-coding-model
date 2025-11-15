import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minTimeToType(self, word: str) -> int:
        # Initial position of the pointer
        current_char = 'a'
        total_time = 0
        
        for char in word:
            # Calculate the clockwise and counterclockwise distances
            clockwise_distance = (ord(char) - ord(current_char)) % 26
            counterclockwise_distance = (ord(current_char) - ord(char)) % 26
            
            # Choose the minimum distance to move the pointer
            move_time = min(clockwise_distance, counterclockwise_distance)
            
            # Add the move time and the time to type the character
            total_time += move_time + 1
            
            # Update the current character to the new one
            current_char = char
        
        return total_time

def minTimeToType(word: str) -> int:
    return Solution().minTimeToType(word)