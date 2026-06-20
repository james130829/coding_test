def solution(a, b):
    z = str(a)
    d = str(b)
    c = z + d
    m = 2*a*b
    if m > int(c):
        return m
    elif int(c) > m:
        return int(c)
    