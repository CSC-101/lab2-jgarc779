def smallest(n:float, m:float) -> float:
    if n < m:
        return n             #none, since 3<2 and 2<2 is F, else is skipped
    else:
        return m
first = smallest(3, 2)  #2
second = smallest(2, 2)  #2, is reasonable because the values are equal and fall under else
print()