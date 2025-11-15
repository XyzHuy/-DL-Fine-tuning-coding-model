import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # Convert each list of companies to a set for easy subset checking
        sets = [set(companies) for companies in favoriteCompanies]
        result = []
        
        # Iterate through each person's list of favorite companies
        for i, set_i in enumerate(sets):
            is_subset = False
            # Compare with every other person's list
            for j, set_j in enumerate(sets):
                if i != j and set_i.issubset(set_j):
                    is_subset = True
                    break
            # If the current list is not a subset of any other, add the index to result
            if not is_subset:
                result.append(i)
        
        return result

def peopleIndexes(favoriteCompanies: List[List[str]]) -> List[int]:
    return Solution().peopleIndexes(favoriteCompanies)