import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Sort the tokens to play the smallest token face-up and the largest token face-down
        tokens.sort()
        score = 0
        max_score = 0
        left, right = 0, len(tokens) - 1
        
        while left <= right:
            # If we have enough power, play the smallest token face-up
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            # If we don't have enough power and we have a score, play the largest token face-down
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                # If we can't play any token, break the loop
                break
        
        return max_score

def bagOfTokensScore(tokens: List[int], power: int) -> int:
    return Solution().bagOfTokensScore(tokens, power)