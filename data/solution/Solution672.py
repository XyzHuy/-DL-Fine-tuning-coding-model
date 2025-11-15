import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # The problem can be simplified by observing patterns.
        # Since the state of the lights is periodic with a period of 3,
        # we only need to consider up to 3 lights.
        n = min(n, 3)
        
        # If no presses are made, only the original state is possible.
        if presses == 0:
            return 1
        
        # Depending on the number of lights and presses, the number of distinct states is limited.
        if n == 1:
            # Only two states: on or off.
            return 2
        elif n == 2:
            # With 1 press, we can get 3 states: [on, off], [off, on], [off, off].
            # With 2 presses, we can get all 4 states.
            return 3 if presses == 1 else 4
        else:
            # For 3 or more lights:
            # With 1 press, we can get 4 states.
            # With 2 presses, we can get 7 states.
            # With 3 or more presses, we can get all 8 states.
            return 4 if presses == 1 else 7 if presses == 2 else 8

def flipLights(n: int, presses: int) -> int:
    return Solution().flipLights(n, presses)