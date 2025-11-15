import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Initialize the result array to store the exclusive time for each function
        exclusive_time = [0] * n
        
        # Stack to keep track of the function calls
        stack = []
        
        # Process each log entry
        for log in logs:
            function_id, status, timestamp = log.split(':')
            function_id = int(function_id)
            timestamp = int(timestamp)
            
            if status == "start":
                # If there is a function already running, calculate its execution time so far
                if stack:
                    prev_id, prev_timestamp = stack[-1]
                    exclusive_time[prev_id] += timestamp - prev_timestamp
                # Push the current function and its timestamp onto the stack
                stack.append((function_id, timestamp))
            else:
                # Pop the function from the stack and calculate its execution time
                prev_id, prev_timestamp = stack.pop()
                exclusive_time[prev_id] += timestamp - prev_timestamp + 1
                # If there is a function in the stack, it resumes execution
                if stack:
                    prev_id, prev_timestamp = stack[-1]
                    stack[-1] = (prev_id, timestamp + 1)
        
        return exclusive_time

def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    return Solution().exclusiveTime(n, logs)