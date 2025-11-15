import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def binaryGap(self, n: int) -> int:
        # Convert the number to its binary representation and strip the '0b' prefix
        binary_representation = bin(n)[2:]
        
        # Initialize variables to track the maximum distance and the last position of '1'
        max_distance = 0
        last_position = -1
        
        # Iterate over the binary representation to find the positions of '1's
        for index, bit in enumerate(binary_representation):
            if bit == '1':
                if last_position != -1:
                    # Calculate the distance between the current '1' and the last '1'
                    distance = index - last_position
                    # Update the maximum distance if the current distance is greater
                    max_distance = max(max_distance, distance)
                # Update the last position to the current index
                last_position = index
        
        return max_distance

def binaryGap(n: int) -> int:
    return Solution().binaryGap(n)