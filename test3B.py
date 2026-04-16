def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             #when a is greater than b and c
    elif b > c:
        return b + c             #when a is not greater than b and c and b > c
    else:
        return 2 * c             #when a is not greater than b and c and b < c


answer1 = function2(3, 2, 1)     #1
answer2 = function2(2, 3, 1)     #4
answer3 = function2(2, 1, 3)     #6
print()