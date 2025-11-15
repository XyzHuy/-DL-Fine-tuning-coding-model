import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # Convert feedback lists to sets for O(1) lookup
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)
        
        # Initialize a list to store (score, id) tuples
        scores = []
        
        # Calculate the score for each student
        for i in range(len(report)):
            score = 0
            words = report[i].split()
            for word in words:
                if word in positive_set:
                    score += 3
                elif word in negative_set:
                    score -= 1
            # Store negative score for easier sorting (max-heap behavior using min-heap)
            scores.append((-score, student_id[i]))
        
        # Sort the scores based on the score (primary) and student_id (secondary)
        scores.sort()
        
        # Extract the top k student ids
        return [student_id for _, student_id in scores[:k]]

def topStudents(positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
    return Solution().topStudents(positive_feedback, negative_feedback, report, student_id, k)