import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        
        m, n = len(image), len(image[0])
        
        # Helper function to check if there is any black pixel in the given row
        def hasBlackPixelRow(row: int) -> bool:
            for col in range(n):
                if image[row][col] == '1':
                    return True
            return False
        
        # Helper function to check if there is any black pixel in the given column
        def hasBlackPixelCol(col: int) -> bool:
            for row in range(m):
                if image[row][col] == '1':
                    return True
            return False
        
        # Binary search to find the topmost row with a black pixel
        top = self.binarySearch(0, x, hasBlackPixelRow, True)
        # Binary search to find the bottommost row with a black pixel
        bottom = self.binarySearch(x, m - 1, hasBlackPixelRow, False)
        # Binary search to find the leftmost column with a black pixel
        left = self.binarySearch(0, y, hasBlackPixelCol, True)
        # Binary search to find the rightmost column with a black pixel
        right = self.binarySearch(y, n - 1, hasBlackPixelCol, False)
        
        # Calculate the area of the rectangle
        return (bottom - top + 1) * (right - left + 1)
    
    def binarySearch(self, low: int, high: int, checkFunc, goLower: bool) -> int:
        while low < high:
            mid = (low + high) // 2
            if checkFunc(mid):
                if goLower:
                    high = mid
                else:
                    low = mid
            else:
                if goLower:
                    low = mid + 1
                else:
                    high = mid - 1
            if low + 1 == high:
                if goLower:
                    if checkFunc(low):
                        return low
                    else:
                        return high
                else:
                    if checkFunc(high):
                        return high
                    else:
                        return low
        return low

def minArea(image: List[List[str]], x: int, y: int) -> int:
    return Solution().minArea(image, x, y)