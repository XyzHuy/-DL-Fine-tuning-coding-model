import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def move(i):
            return (i + nums[i]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            slow, fast = i, i
            direction = nums[i] > 0
            
            while True:
                next_slow = move(slow)
                if nums[next_slow] == 0 or (nums[next_slow] > 0) != direction:
                    break
                slow = next_slow
                
                next_fast = move(fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break
                fast = move(next_fast)
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
                if slow == fast:
                    if slow == move(slow):
                        break
                    return True
            
            slow = i
            while nums[slow] != 0 and (nums[slow] > 0) == direction:
                next_slow = move(slow)
                nums[slow] = 0
                slow = next_slow
        
        return False

def circularArrayLoop(nums: List[int]) -> bool:
    return Solution().circularArrayLoop(nums)