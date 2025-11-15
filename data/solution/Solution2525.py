import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky_criteria = max(length, width, height) >= 10**4 or (length * width * height) >= 10**9
        heavy_criteria = mass >= 100
        
        if bulky_criteria and heavy_criteria:
            return "Both"
        elif bulky_criteria:
            return "Bulky"
        elif heavy_criteria:
            return "Heavy"
        else:
            return "Neither"

def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    return Solution().categorizeBox(length, width, height, mass)