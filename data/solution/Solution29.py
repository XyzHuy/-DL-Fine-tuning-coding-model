
def divide( dividend, divisor):
    import math
    if divisor == 0:
        return 2**63 - 1
    if dividend == 0:
        return 0
    isPositive = (dividend < 0) == (divisor < 0)
    m = abs(dividend)
    n = abs(divisor)
    # ln and exp
    res = math.log(m) - math.log(n)
    res = int(math.exp(res))
    if isPositive:
        return min(res, 2147483647)
    return max(0 - res, -2147483648)
