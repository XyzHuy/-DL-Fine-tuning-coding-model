def hasCycle(course, deps, visited, tracker):
    visited.add(course)
    tracker.add(course)
    for n in deps[course]:
        if n not in visited and hasCycle(n, deps, visited, tracker):
            return True
        if n in tracker:
            return True
    tracker.remove(course)
    return False

def canFinish(numCourses, prerequisites):
    from collections import defaultdict
    deps = defaultdict(set)
    for course, pre in prerequisites:
        deps[pre].add(course)

    visited = set()
    for course in range(numCourses):
        tracker = set()
        if hasCycle(course, deps, visited, tracker):
            return False
    
    return True