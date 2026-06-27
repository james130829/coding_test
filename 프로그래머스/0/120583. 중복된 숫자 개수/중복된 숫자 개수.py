def solution(array, n):
    b = 0
    for a in array:
        if a == n:
            b+= 1
    return b