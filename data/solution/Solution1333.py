import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # Filter the restaurants based on the given criteria
        filtered_restaurants = [
            restaurant for restaurant in restaurants
            if (not veganFriendly or restaurant[2] == veganFriendly) and
            restaurant[3] <= maxPrice and
            restaurant[4] <= maxDistance
        ]
        
        # Sort the filtered restaurants by rating (descending) and then by id (descending)
        filtered_restaurants.sort(key=lambda x: (-x[1], -x[0]))
        
        # Extract the restaurant IDs from the sorted list
        return [restaurant[0] for restaurant in filtered_restaurants]

def filterRestaurants(restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    return Solution().filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)