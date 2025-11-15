import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort tasks based on the difference between minimum energy required and actual energy spent
        tasks.sort(key=lambda x: (x[1] - x[0], x[1]), reverse=True)
        
        current_energy = 0
        required_energy = 0
        
        for actual, minimum in tasks:
            # If current energy is less than the minimum required, we need to increase our starting energy
            if current_energy < minimum:
                required_energy += (minimum - current_energy)
                current_energy = minimum
            # Spend the actual energy for the task
            current_energy -= actual
        
        return required_energy

def minimumEffort(tasks: List[List[int]]) -> int:
    return Solution().minimumEffort(tasks)