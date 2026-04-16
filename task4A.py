from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    #False, True
    if test:                            #It prevents an index error
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     #None
second = checked_access([1, 0, 1], 2)    #1
print()