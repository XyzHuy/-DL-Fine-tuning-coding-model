import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        # Start with the first element of the sequence
        current_sequence = "1"
        
        # Generate the sequence iteratively from 2 to n
        for _ in range(2, n + 1):
            next_sequence = ""
            i = 0
            while i < len(current_sequence):
                count = 1
                # Count the number of times the current character repeats
                while i + 1 < len(current_sequence) and current_sequence[i] == current_sequence[i + 1]:
                    count += 1
                    i += 1
                # Append the count and the character to the next sequence
                next_sequence += str(count) + current_sequence[i]
                i += 1
            # Update the current sequence to the next sequence
            current_sequence = next_sequence
        
        return current_sequence

def countAndSay(n: int) -> str:
    return Solution().countAndSay(n)