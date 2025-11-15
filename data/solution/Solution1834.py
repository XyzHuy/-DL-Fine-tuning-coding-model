import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add the original indices to the tasks
        tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        # Sort tasks by enqueue time, then by process time, then by index
        tasks.sort()
        
        # Min-heap to store tasks that are available to be processed
        available_tasks = []
        # Result list to store the order of task processing
        result = []
        # Current time
        current_time = 0
        # Task index
        i = 0
        n = len(tasks)
        
        while i < n or available_tasks:
            # If there are no tasks available to process and the current time is less than the next task's enqueue time
            if not available_tasks and current_time < tasks[i][0]:
                # Move the current time to the next task's enqueue time
                current_time = tasks[i][0]
            
            # Add all tasks that are available to be processed at the current time
            while i < n and tasks[i][0] <= current_time:
                # Push the task (processing time, original index) to the heap
                heapq.heappush(available_tasks, (tasks[i][1], tasks[i][2]))
                i += 1
            
            # Pop the task with the shortest processing time (and smallest index if tie) from the heap
            process_time, task_index = heapq.heappop(available_tasks)
            # Add the task index to the result
            result.append(task_index)
            # Update the current time after processing the task
            current_time += process_time
        
        return result

def getOrder(tasks: List[List[int]]) -> List[int]:
    return Solution().getOrder(tasks)