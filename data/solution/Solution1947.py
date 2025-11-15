import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def compatibility_score(s, m):
            return sum(a == b for a, b in zip(s, m))
        
        def backtrack(student_index, used_mentors):
            if student_index == len(students):
                return 0
            
            max_score = 0
            for mentor_index in range(len(mentors)):
                if not used_mentors[mentor_index]:
                    used_mentors[mentor_index] = True
                    score = compatibility_score(students[student_index], mentors[mentor_index])
                    max_score = max(max_score, score + backtrack(student_index + 1, used_mentors))
                    used_mentors[mentor_index] = False
            
            return max_score
        
        used_mentors = [False] * len(mentors)
        return backtrack(0, used_mentors)

def maxCompatibilitySum(students: List[List[int]], mentors: List[List[int]]) -> int:
    return Solution().maxCompatibilitySum(students, mentors)