import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict
        
        # Dictionary to hold lists of people for each group size
        size_to_people = defaultdict(list)
        
        # Populate the dictionary
        for person, size in enumerate(groupSizes):
            size_to_people[size].append(person)
        
        # Create the result list
        result = []
        
        # Form groups from the dictionary
        for size, people in size_to_people.items():
            # Split the list of people into sublists of the required size
            for i in range(0, len(people), size):
                result.append(people[i:i + size])
        
        return result

def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    return Solution().groupThePeople(groupSizes)