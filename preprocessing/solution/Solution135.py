def singleNumber(nums):
    # bitmask
    # ones as a bitmask to represent the ith bit had appeared once.
    # twos as a bitmask to represent the ith bit had appeared twice.
    # threes as a bitmask to represent the ith bit had appeared three times.
    ones, twos, threes = 0, 0, 0
    for num in nums:
        twos |= ones & num
        ones ^= num
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes
    return ones
