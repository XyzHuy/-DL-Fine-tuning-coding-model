import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Dictionary to hold scores for each student
        scores = defaultdict(list)
        
        # Collect scores for each student
        for student_id, score in items:
            scores[student_id].append(score)
        
        # Calculate the top five average for each student
        result = []
        for student_id in sorted(scores.keys()):
            # Get the top five scores, sort them in descending order and take the first five
            top_five_scores = sorted(scores[student_id], reverse=True)[:5]
            # Calculate the average using integer division
            top_five_average = sum(top_five_scores) // 5
            # Append the result as [student_id, top_five_average]
            result.append([student_id, top_five_average])
        
        return result

def highFive(items: List[List[int]]) -> List[List[int]]:
    return Solution().highFive(items)