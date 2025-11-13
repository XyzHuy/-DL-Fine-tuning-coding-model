def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ls = len(height)
    if ls == 0:
        return 0
    res, left = 0, 0
    while left < ls and height[left] == 0:
        left += 1
    pos = left + 1
    while pos < ls:
        if height[pos] >= height[left]:
            # there is a right bar which is no less than left bar
            res += rain_water(height, left, pos)
            left = pos
            pos += 1
        elif pos == ls - 1:
            # left bar is higher than all right bar
            max_value, max_index = 0, pos
            for index in range(left + 1, ls):
                if height[index] > max_value:
                    max_value = height[index]
                    max_index = index
            res += rain_water(height, left, max_index)
            left = max_index
            pos = left + 1
        else:
            pos += 1
    return res

def rain_water( height, start, end):
    # computer rain water
    if end - start <= 1:
        return 0
    min_m = min(height[start], height[end])
    res = min_m * (end - start - 1)
    step = 0
    for index in range(start + 1, end):
        if height[index] > 0:
            step += height[index]
    return res - step