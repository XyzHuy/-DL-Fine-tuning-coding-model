def selfDividingNumbers(left: int, right: int) -> list[int]:
    # check every digit
    return [x for x in range(left, right+1) if all([int(i) != 0 and x % int(i)==0 for i in str(x)])]
