import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Dictionary to map colors to sets of balls
        color_to_balls = {}
        # Result list to store the number of colors after each query
        result = []
        # Set to keep track of colored balls
        colored_balls = set()
        
        for x, y in queries:
            if x in colored_balls:
                # Find the current color of ball x
                old_color = None
                for color, balls in color_to_balls.items():
                    if x in balls:
                        old_color = color
                        balls.remove(x)
                        if not balls:
                            del color_to_balls[color]
                        break
            
            # Add the ball to the new color set
            if y not in color_to_balls:
                color_to_balls[y] = set()
            color_to_balls[y].add(x)
            colored_balls.add(x)
            
            # Append the number of unique colors to the result
            result.append(len(color_to_balls))
        
        return result

def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    return Solution().queryResults(limit, queries)