import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Sort the asteroids by their mass in ascending order
        asteroids.sort()
        
        # Iterate through the sorted asteroids
        for asteroid in asteroids:
            # If the planet's mass is less than the asteroid's mass, return False
            if mass < asteroid:
                return False
            # Otherwise, the planet destroys the asteroid and gains its mass
            mass += asteroid
        
        # If all asteroids are destroyed, return True
        return True

def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    return Solution().asteroidsDestroyed(mass, asteroids)