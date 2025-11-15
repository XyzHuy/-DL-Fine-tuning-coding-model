import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort people by height in descending order, and by k in ascending order
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        # Insert each person into the queue at the index specified by their k value
        for person in people:
            queue.insert(person[1], person)
        
        return queue

def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    return Solution().reconstructQueue(people)