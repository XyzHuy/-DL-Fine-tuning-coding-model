def largestDivisibleSubset(nums):
    ls = len(nums)
    S = {-1: set()}
    for num in sorted(nums):
        candicate = []
        for key in S:
            if num % key == 0:
                candicate.append(S[key])
        # max previous with curr
        S[num] = max(candicate, key=len) | {num}
    return
