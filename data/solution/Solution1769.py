import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # Count the number of balls to the left and right of each position
        balls_to_left = 0
        balls_to_right = 0
        
        # Calculate the initial number of operations for the first box
        for i in range(1, n):
            if boxes[i] == '1':
                answer[0] += i
                balls_to_right += 1
        
        # Use the result of the previous box to calculate the current box
        for i in range(1, n):
            if boxes[i - 1] == '1':
                balls_to_left += 1
            answer[i] = answer[i - 1] + balls_to_left - balls_to_right
            if boxes[i] == '1':
                balls_to_right -= 1
        
        return answer

def minOperations(boxes: str) -> List[int]:
    return Solution().minOperations(boxes)