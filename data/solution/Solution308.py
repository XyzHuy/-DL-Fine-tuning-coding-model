def isOneBitCharacter(bits: list[int]) -> bool:
    pos = 0
    # Go through bits
    while pos < len(bits) - 1:
        # if 1, pos + 2; if 0, pos + 1
        pos += bits[pos] + 1
    return pos == len(bits) - 1
