import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
    return Solution().findDelayedArrivalTime(arrivalTime, delayedTime)