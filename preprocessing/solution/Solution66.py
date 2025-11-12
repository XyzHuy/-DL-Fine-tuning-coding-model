def plusOne( digits):
    ls = len(digits)
    for index in reversed(range(ls)):
        if digits[index] < 9:
            digits[index] += 1
            # do not need to continue
            return digits
        else:
            # 10
            digits[index] = 0
    digits.insert(0, 1)
    return digits
