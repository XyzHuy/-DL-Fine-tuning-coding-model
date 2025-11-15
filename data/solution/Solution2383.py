import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        total_energy_needed = sum(energy) + 1
        energy_training_hours = max(0, total_energy_needed - initialEnergy)
        
        current_experience = initialExperience
        experience_training_hours = 0
        
        for opponent_exp in experience:
            if current_experience <= opponent_exp:
                experience_needed = opponent_exp + 1 - current_experience
                experience_training_hours += experience_needed
                current_experience += experience_needed
            
            current_experience += opponent_exp
        
        return energy_training_hours + experience_training_hours

def minNumberOfHours(initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
    return Solution().minNumberOfHours(initialEnergy, initialExperience, energy, experience)