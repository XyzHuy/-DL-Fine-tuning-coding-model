import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort points by x-coordinate, and by y-coordinate in descending order if x-coordinates are the same
        points.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        n = len(points)
        
        # Iterate over all pairs of points
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Check if point i is on the upper left of point j
                if x1 <= x2 and y1 >= y2:
                    # Check if there are no points in the rectangle (x1, y1) to (x2, y2)
                    valid = True
                    for k in range(i + 1, j):
                        xk, yk = points[k]
                        if x1 <= xk <= x2 and y2 <= yk <= y1:
                            valid = False
                            break
                    if valid:
                        count += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.numberOfPairs([[6,2],[4,4],[2,6]]))  # Output: 2

def numberOfPairs(points: List[List[int]]) -> int:
    return Solution().numberOfPairs(points)