import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        from collections import defaultdict, deque

        # Create a graph where each recipe points to its dependent recipes
        graph = defaultdict(list)
        # Create an indegree map to count how many ingredients are needed for each recipe
        indegree = defaultdict(int)
        
        # Populate the graph and indegree map
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                indegree[recipe] += 1
        
        # Initialize the queue with all the supplies
        queue = deque(supplies)
        result = []
        
        # Process the queue
        while queue:
            supply = queue.popleft()
            for recipe in graph[supply]:
                indegree[recipe] -= 1
                # If all ingredients for a recipe are available, add it to the result and queue
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
        
        return result

def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    return Solution().findAllRecipes(recipes, ingredients, supplies)