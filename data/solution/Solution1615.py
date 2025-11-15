import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Create an adjacency list to store the roads connected to each city
        adjacency_list = defaultdict(set)
        
        for a, b in roads:
            adjacency_list[a].add(b)
            adjacency_list[b].add(a)
        
        # Find the cities with the highest and second highest number of roads
        degree = [(len(adjacency_list[i]), i) for i in range(n)]
        degree.sort(reverse=True)
        
        max_degree = degree[0][0]
        cities_with_max_degree = [city for degree, city in degree if degree == max_degree]
        
        if len(cities_with_max_degree) > 1:
            # If there is more than one city with the maximum degree, we can choose any two of them
            # and check if they are directly connected
            for i in range(len(cities_with_max_degree)):
                for j in range(i + 1, len(cities_with_max_degree)):
                    city1, city2 = cities_with_max_degree[i], cities_with_max_degree[j]
                    if city2 not in adjacency_list[city1]:
                        return max_degree * 2
            # If all pairs of cities with the maximum degree are directly connected, 
            # we return max_degree * 2 - 1
            return max_degree * 2 - 1
        else:
            # If there is only one city with the maximum degree, we need to find the city with the second highest degree
            second_max_degree = degree[len(cities_with_max_degree)][0]
            cities_with_second_max_degree = [city for degree, city in degree if degree == second_max_degree]
            
            # Check each city with the second highest degree to see if it is connected to the city with the maximum degree
            max_city = cities_with_max_degree[0]
            for city in cities_with_second_max_degree:
                if city not in adjacency_list[max_city]:
                    return max_degree + second_max_degree
            
            # If all cities with the second highest degree are connected to the city with the maximum degree,
            # we return max_degree + second_max_degree - 1
            return max_degree + second_max_degree - 1

def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    return Solution().maximalNetworkRank(n, roads)