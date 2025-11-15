import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Initialize a set to keep track of friends who have received the ball
        received_ball = set()
        # Start with the first friend
        current_friend = 0
        # Initialize the step multiplier
        step_multiplier = 1
        
        # Loop until a friend receives the ball for the second time
        while current_friend not in received_ball:
            # Mark the current friend as having received the ball
            received_ball.add(current_friend)
            # Calculate the next friend to receive the ball
            current_friend = (current_friend + step_multiplier * k) % n
            # Increment the step multiplier
            step_multiplier += 1
        
        # The losers are the friends who never received the ball
        losers = [i + 1 for i in range(n) if i not in received_ball]
        
        return losers

def circularGameLosers(n: int, k: int) -> List[int]:
    return Solution().circularGameLosers(n, k)