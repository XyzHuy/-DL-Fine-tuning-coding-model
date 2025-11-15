import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        adjacent_count = 0
        result = []

        for index, color in queries:
            # Check the left neighbor
            if index > 0:
                if colors[index] != 0 and colors[index] == colors[index - 1]:
                    adjacent_count -= 1
                if color == colors[index - 1]:
                    adjacent_count += 1

            # Check the right neighbor
            if index < n - 1:
                if colors[index] != 0 and colors[index] == colors[index + 1]:
                    adjacent_count -= 1
                if color == colors[index + 1]:
                    adjacent_count += 1

            # Update the color at the current index
            colors[index] = color

            # Append the current adjacent count to the result
            result.append(adjacent_count)

        return result

def colorTheArray(n: int, queries: List[List[int]]) -> List[int]:
    return Solution().colorTheArray(n, queries)