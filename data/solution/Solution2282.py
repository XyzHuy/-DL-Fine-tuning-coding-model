import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        def count_visible_people(line):
            stack = []
            result = [0] * len(line)
            for i in range(len(line) - 1, -1, -1):
                while stack and stack[-1] < line[i]:
                    result[i] += 1
                    stack.pop()
                if stack:
                    result[i] += 1
                if stack and stack[-1] == line[i]:
                    stack.pop()
                stack.append(line[i])
            return result
        
        m, n = len(heights), len(heights[0])
        answer = [[0] * n for _ in range(m)]
        
        # Check for each row
        for i in range(m):
            row_counts = count_visible_people(heights[i])
            for j in range(n):
                answer[i][j] += row_counts[j]
        
        # Check for each column
        for j in range(n):
            col = [heights[i][j] for i in range(m)]
            col_counts = count_visible_people(col)
            for i in range(m):
                answer[i][j] += col_counts[i]
        
        return answer

def seePeople(heights: List[List[int]]) -> List[List[int]]:
    return Solution().seePeople(heights)