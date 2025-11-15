import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        # Calculate the sum of digits and count of '?' in the first and second half
        left_sum = 0
        left_question_marks = 0
        right_sum = 0
        right_question_marks = 0
        
        for i in range(half):
            if num[i] == '?':
                left_question_marks += 1
            else:
                left_sum += int(num[i])
        
        for i in range(half, n):
            if num[i] == '?':
                right_question_marks += 1
            else:
                right_sum += int(num[i])
        
        # If the total number of question marks is odd, Alice can always win by making the sums unequal
        if (left_question_marks + right_question_marks) % 2 == 1:
            return True
        
        # Calculate the total sum needed to balance the equation
        left_needed = left_sum + left_question_marks * 4.5  # Each '?' can contribute 0 to 9, so 4.5 is the average
        right_needed = right_sum + right_question_marks * 4.5
        
        # If the sums are not equal, Alice wins
        return left_needed != right_needed

def sumGame(num: str) -> bool:
    return Solution().sumGame(num)