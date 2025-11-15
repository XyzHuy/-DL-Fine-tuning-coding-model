import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def canWin(nums, memo):
            if not nums:
                return 0
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            
            # Player 1 can choose either the first or the last number
            # If player 1 chooses the first number, the score difference will be:
            # nums[0] - the score difference player 1 can get from the remaining numbers
            # If player 1 chooses the last number, the score difference will be:
            # nums[-1] - the score difference player 1 can get from the remaining numbers
            score_diff_if_pick_first = nums[0] - canWin(nums[1:], memo)
            score_diff_if_pick_last = nums[-1] - canWin(nums[:-1], memo)
            
            # Player 1 will choose the option that maximizes the score difference
            score_diff = max(score_diff_if_pick_first, score_diff_if_pick_last)
            memo[tuple(nums)] = score_diff
            return score_diff
        
        memo = {}
        return canWin(nums, memo) >= 0

def predictTheWinner(nums: List[int]) -> bool:
    return Solution().predictTheWinner(nums)