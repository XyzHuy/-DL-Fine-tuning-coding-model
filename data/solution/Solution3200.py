import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # Function to calculate the maximum height of the triangle
        def max_height_with_color(start_color, red, blue):
            height = 0
            current_color = start_color
            while True:
                balls_needed = height + 1
                if current_color == 'red':
                    if red < balls_needed:
                        break
                    red -= balls_needed
                else:
                    if blue < balls_needed:
                        break
                    blue -= balls_needed
                height += 1
                current_color = 'blue' if current_color == 'red' else 'red'
            return height

        # Try starting with red at the top and blue at the top
        height_starting_red = max_height_with_color('red', red, blue)
        height_starting_blue = max_height_with_color('blue', red, blue)

        # Return the maximum height achievable
        return max(height_starting_red, height_starting_blue)

def maxHeightOfTriangle(red: int, blue: int) -> int:
    return Solution().maxHeightOfTriangle(red, blue)