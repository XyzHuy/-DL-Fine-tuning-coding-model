import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                # If we are at or before k, we count the min of tickets[i] and tickets[k]
                time += min(tickets[i], tickets[k])
            else:
                # If we are after k, we count the min of tickets[i] and tickets[k] - 1
                # because the person at position k will have one less ticket to buy after their turn
                time += min(tickets[i], tickets[k] - 1)
        return time

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    return Solution().timeRequiredToBuy(tickets, k)