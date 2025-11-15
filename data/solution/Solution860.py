import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize the count of $5 and $10 bills
        five_count = 0
        ten_count = 0
        
        # Iterate through each bill in the list
        for bill in bills:
            if bill == 5:
                # If the bill is $5, we just take it
                five_count += 1
            elif bill == 10:
                # If the bill is $10, we need to give back $5
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1
            elif bill == 20:
                # If the bill is $20, we prefer to give back one $10 and one $5
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    # If we don't have a $10 bill, we give back three $5 bills
                    five_count -= 3
                else:
                    return False
        
        # If we can give back change to all customers, return True
        return True

def lemonadeChange(bills: List[int]) -> bool:
    return Solution().lemonadeChange(bills)