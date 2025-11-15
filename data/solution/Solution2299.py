import collections
import string
import math
import datetime


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # Check if the password has at least 8 characters
        if len(password) < 8:
            return False
        
        # Define the set of special characters
        special_chars = set("!@#$%^&*()-+")
        
        # Initialize flags for each requirement
        has_lower = has_upper = has_digit = has_special = False
        
        # Iterate through the password to check each character
        for i, char in enumerate(password):
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True
            
            # Check for adjacent identical characters
            if i > 0 and password[i] == password[i - 1]:
                return False
        
        # Check if all conditions are met
        return has_lower and has_upper and has_digit and has_special

def strongPasswordCheckerII(password: str) -> bool:
    return Solution().strongPasswordCheckerII(password)