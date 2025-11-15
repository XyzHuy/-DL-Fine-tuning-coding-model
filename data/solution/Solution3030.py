import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def is_valid_region(i, j):
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if x < i + 2 and abs(image[x][y] - image[x + 1][y]) > threshold:
                        return False
                    if y < j + 2 and abs(image[x][y] - image[x][y + 1]) > threshold:
                        return False
            return True

        def calculate_average(i, j):
            total = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    total += image[x][y]
            return total // 9

        m, n = len(image), len(image[0])
        result = [[0] * n for _ in range(m)]
        count = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                if is_valid_region(i, j):
                    avg = calculate_average(i, j)
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            result[x][y] += avg
                            count[x][y] += 1

        for i in range(m):
            for j in range(n):
                if count[i][j] == 0:
                    result[i][j] = image[i][j]
                else:
                    result[i][j] //= count[i][j]

        return result

def resultGrid(image: List[List[int]], threshold: int) -> List[List[int]]:
    return Solution().resultGrid(image, threshold)