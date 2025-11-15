import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        def calculate_correct_answer(s):
            stack = []
            current_number = 0
            current_operator = '+'
            
            for i, char in enumerate(s):
                if char.isdigit():
                    current_number = current_number * 10 + int(char)
                
                if not char.isdigit() or i == len(s) - 1:
                    if current_operator == '+':
                        stack.append(current_number)
                    elif current_operator == '*':
                        stack[-1] *= current_number
                    current_operator = char
                    current_number = 0
            
            return sum(stack)
        
        @lru_cache(None)
        def get_possible_answers(sub_expr):
            if sub_expr.isdigit():
                return {int(sub_expr)}
            
            possible_results = set()
            for i, char in enumerate(sub_expr):
                if char in "+*":
                    left_results = get_possible_answers(sub_expr[:i])
                    right_results = get_possible_answers(sub_expr[i+1:])
                    
                    for left in left_results:
                        for right in right_results:
                            result = left + right if char == '+' else left * right
                            if result <= 1000:  # Since answers are bounded by 1000
                                possible_results.add(result)
            return possible_results
        
        correct_answer = calculate_correct_answer(s)
        possible_answers = get_possible_answers(s)
        
        score = 0
        for answer in answers:
            if answer == correct_answer:
                score += 5
            elif answer in possible_answers:
                score += 2
        
        return score

def scoreOfStudents(s: str, answers: List[int]) -> int:
    return Solution().scoreOfStudents(s, answers)