import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Convert the images to lists of coordinates where the value is 1
        points1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        points2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        
        # Dictionary to count the frequency of each translation vector
        translation_count = defaultdict(int)
        
        # Calculate the translation vector for each pair of points
        for x1, y1 in points1:
            for x2, y2 in points2:
                translation_vector = (x2 - x1, y2 - y1)
                translation_count[translation_vector] += 1
        
        # The maximum value in the dictionary is the largest overlap
        return max(translation_count.values(), default=0)

def largestOverlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    return Solution().largestOverlap(img1, img2)