import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        # Create a list to track the start and end of the range for which a number contributes to the score
        points = [0] * (n + 1)
        
        for i, num in enumerate(nums):
            if num > i:
                # If num > i, it will contribute to the score after it has rotated past index i
                points[(i + 1) % n] += 1
                points[(i - num + n + 1) % n] -= 1
            else:
                # If num <= i, it contributes to the score from the start until it rotates past index i - num
                points[0] += 1
                points[(i - num + 1) % n] -= 1
                points[(i + 1) % n] += 1
        
        # Calculate the prefix sum to find the score for each rotation
        for i in range(1, n):
            points[i] += points[i - 1]
        
        # Find the rotation index with the maximum score
        max_score = max(points)
        for i, score in enumerate(points):
            if score == max_score:
                return i
            
        return 0

def bestRotation(nums: List[int]) -> int:
    return Solution().bestRotation(nums)