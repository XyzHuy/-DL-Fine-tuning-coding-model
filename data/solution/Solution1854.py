import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Create a list to store population changes
        population_changes = [0] * 101  # From 1950 to 2050 is a span of 101 years
        
        # Process each log entry
        for birth, death in logs:
            birth_year_index = birth - 1950
            death_year_index = death - 1950
            population_changes[birth_year_index] += 1
            if death_year_index < 101:  # Ensure we don't go out of bounds
                population_changes[death_year_index] -= 1
        
        # Calculate the population for each year and find the year with the maximum population
        max_population = 0
        current_population = 0
        earliest_year = 1950
        
        for year in range(101):
            current_population += population_changes[year]
            if current_population > max_population:
                max_population = current_population
                earliest_year = year + 1950
        
        return earliest_year

def maximumPopulation(logs: List[List[int]]) -> int:
    return Solution().maximumPopulation(logs)