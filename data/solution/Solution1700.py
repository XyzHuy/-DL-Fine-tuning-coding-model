import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unable_to_eat = 0
        
        while sandwiches:
            if unable_to_eat == len(students):
                break
            
            student = students.pop(0)
            if student == sandwiches[0]:
                sandwiches.pop(0)
                unable_to_eat = 0  # Reset the counter if a student takes a sandwich
            else:
                students.append(student)
                unable_to_eat += 1
        
        return unable_to_eat

def countStudents(students: List[int], sandwiches: List[int]) -> int:
    return Solution().countStudents(students, sandwiches)