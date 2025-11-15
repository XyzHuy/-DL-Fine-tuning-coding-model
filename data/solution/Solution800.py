import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def similarRGB(self, color: str) -> str:
        # Helper function to find the closest shorthand value
        def closest_shorthand(hex_val):
            # Convert hex value to integer
            num = int(hex_val, 16)
            # Find the closest multiple of 17 (0x11 in hex)
            closest = round(num / 17) * 17
            # Convert back to hex and ensure it's two characters long
            return f"{closest:02x}"
        
        # Process each pair of hex digits
        closest_color = "#"
        for i in range(1, 7, 2):
            closest_color += closest_shorthand(color[i:i+2])
        
        return closest_color

def similarRGB(color: str) -> str:
    return Solution().similarRGB(color)