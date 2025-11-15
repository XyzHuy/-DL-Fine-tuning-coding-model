import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Define a max heap based on the potential increase in pass ratio
        def potential_increase(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        
        # Create a max heap with the negative of the potential increase
        max_heap = []
        for passed, total in classes:
            heapq.heappush(max_heap, (-potential_increase(passed, total), passed, total))
        
        # Assign extra students to the class that benefits the most
        for _ in range(extraStudents):
            increase, passed, total = heapq.heappop(max_heap)
            passed += 1
            total += 1
            heapq.heappush(max_heap, (-potential_increase(passed, total), passed, total))
        
        # Calculate the final average pass ratio
        final_ratio = sum(passed / total for _, passed, total in max_heap) / len(classes)
        return final_ratio

def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:
    return Solution().maxAverageRatio(classes, extraStudents)