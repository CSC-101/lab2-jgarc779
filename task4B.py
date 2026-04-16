def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # len(L) > 2
    elif len(L) > 1:                                  # len("this) + len("is) + len("the") [4+2+3=9]
        result = len(L[0]) + len(L[1])                # len(L) > 1
    elif len(L) > 0:                                  # None
        result = len(L[0])                            # len(L) > 1
    else:                                             # len("another") + len("call") [7+4=11]
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()