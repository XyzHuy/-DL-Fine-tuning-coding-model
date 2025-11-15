import collections
import string
import math
import datetime


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Split the input by new line to get each line
        lines = input.split('\n')
        # Dictionary to store the cumulative length of the path at each depth
        path_length = {0: 0}
        max_length = 0

        for line in lines:
            # Count the number of tabs to determine the depth
            depth = line.count('\t')
            # Remove the tabs to get the actual name
            name = line[depth:]
            
            # If it's a file, calculate the total length of the path
            if '.' in name:
                # Calculate the total path length including slashes
                total_length = path_length[depth] + len(name)
                # Update max_length if this path is longer
                max_length = max(max_length, total_length)
            else:
                # If it's a directory, update the path_length dictionary
                # +1 for the slash that would be added in the path
                path_length[depth + 1] = path_length[depth] + len(name) + 1
        
        return max_length

def lengthLongestPath(input: str) -> int:
    return Solution().lengthLongestPath(input)