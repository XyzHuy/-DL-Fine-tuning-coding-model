import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        enter_queue = deque()
        exit_queue = deque()
        result = [0] * n
        last_used = -1  # -1: unused, 0: enter, 1: exit
        current_time = 0
        i = 0

        while i < n or enter_queue or exit_queue:
            # Add new people to the respective queues
            while i < n and arrival[i] <= current_time:
                if state[i] == 0:
                    enter_queue.append(i)
                else:
                    exit_queue.append(i)
                i += 1

            # Decide who to let through the door
            if exit_queue and (last_used == 1 or last_used == -1 or not enter_queue):
                person = exit_queue.popleft()
                result[person] = current_time
                last_used = 1
            elif enter_queue:
                person = enter_queue.popleft()
                result[person] = current_time
                last_used = 0
            else:
                last_used = -1  # Door was unused

            # Move to the next second
            if i < n and not enter_queue and not exit_queue:
                current_time = arrival[i]
            else:
                current_time += 1

        return result

def timeTaken(arrival: List[int], state: List[int]) -> List[int]:
    return Solution().timeTaken(arrival, state)