import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        index = 0
        
        while index < len(heights):
            # If this bar is higher than the bar that was previous bar, push it to stack
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Calculate area of all bars with height stack top. The bar at stack top is the smallest (or minimum height) bar. 'index' is 'right index' for the top and element before top in stack is 'left index'
                top_of_stack = stack.pop()
                # Calculate the area with heights[top_of_stack] stack as smallest (or minimum height) bar. 'index' is 'right index' for the top and element before top in stack is 'left index'
                area = (heights[top_of_stack] * 
                       ((index - stack[-1] - 1) if stack else index))
                # Update max area, if needed
                max_area = max(max_area, area)
        
        # Now pop the remaining bars from stack and calculate area with every popped bar as the smallest bar
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * 
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
        
        return max_area

def largestRectangleArea(heights: List[int]) -> int:
    return Solution().largestRectangleArea(heights)