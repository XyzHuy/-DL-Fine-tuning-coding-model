import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # If we don't have enough money to give each child at least 1 dollar, return -1
        if money < children:
            return -1
        
        # Subtract 1 dollar from each child to ensure everyone gets at least 1 dollar
        money -= children
        
        # Calculate the maximum number of children who can get exactly 7 more dollars (total 8 dollars)
        max_eight_dollar_children = money // 7
        remaining_money = money % 7
        
        # If we have more children who can get 8 dollars than the actual number of children, 
        # then the last child will have more than 8 dollars, so we can only give 8 dollars to (children - 1) children
        if max_eight_dollar_children > children:
            return children - 1
        
        # If we have exactly the number of children who can get 8 dollars, 
        # but there is some remaining money, the last child will have more than 8 dollars, 
        # so we can only give 8 dollars to (children - 1) children
        if max_eight_dollar_children == children and remaining_money > 0:
            return children - 1
        
        # If we have one child left and exactly 3 dollars remaining, we cannot give this child 8 dollars, 
        # so we can only give 8 dollars to (children - 1) children
        if max_eight_dollar_children == children - 1 and remaining_money == 3:
            return children - 2
        
        return max_eight_dollar_children

def distMoney(money: int, children: int) -> int:
    return Solution().distMoney(money, children)