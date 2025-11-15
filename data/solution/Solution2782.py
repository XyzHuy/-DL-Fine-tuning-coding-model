import random
import functools
import collections
import string
import math
import datetime


# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        categories = set()
        
        for i in range(n):
            found_category = False
            for cat in categories:
                if categoryHandler.haveSameCategory(i, cat):
                    found_category = True
                    break
            if not found_category:
                categories.add(i)
        
        return len(categories)

def numberOfCategories(n: int, categoryHandler: Optional['CategoryHandler']) -> int:
    return Solution().numberOfCategories(n, categoryHandler)