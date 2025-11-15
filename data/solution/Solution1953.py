import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # Find the maximum number of milestones in a single project
        max_milestones = max(milestones)
        # Calculate the sum of milestones in all other projects
        rest_milestones = sum(milestones) - max_milestones
        
        # If the maximum milestones in a single project is more than the sum of all other milestones plus one,
        # we can only work on other projects until they are finished, then switch to the largest project
        # and work on it for 'rest_milestones + 1' weeks.
        if max_milestones > rest_milestones + 1:
            return rest_milestones * 2 + 1
        else:
            # Otherwise, we can alternate between the largest project and other projects until all are finished.
            return rest_milestones + max_milestones

def numberOfWeeks(milestones: List[int]) -> int:
    return Solution().numberOfWeeks(milestones)