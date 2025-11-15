import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]

def convertTemperature(celsius: float) -> List[float]:
    return Solution().convertTemperature(celsius)