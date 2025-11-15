import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_to_odd_indices(s, a):
            # Convert string to list for easy manipulation
            s_list = list(s)
            for i in range(1, len(s), 2):
                # Add a to the digit at the odd index and take modulo 10
                s_list[i] = str((int(s_list[i]) + a) % 10)
            return ''.join(s_list)
        
        def rotate_string(s, b):
            # Rotate the string by b positions to the right
            return s[-b:] + s[:-b]
        
        # Use a set to keep track of seen strings to avoid infinite loops
        seen = set()
        # Use a list as a queue for BFS
        queue = [s]
        seen.add(s)
        smallest = s
        
        while queue:
            current = queue.pop(0)
            # Check if the current string is lexicographically smaller
            if current < smallest:
                smallest = current
            
            # Generate the new string by adding a to all odd indices
            add_result = add_to_odd_indices(current, a)
            if add_result not in seen:
                seen.add(add_result)
                queue.append(add_result)
            
            # Generate the new string by rotating the string by b positions
            rotate_result = rotate_string(current, b)
            if rotate_result not in seen:
                seen.add(rotate_result)
                queue.append(rotate_result)
        
        return smallest

def findLexSmallestString(s: str, a: int, b: int) -> str:
    return Solution().findLexSmallestString(s, a, b)