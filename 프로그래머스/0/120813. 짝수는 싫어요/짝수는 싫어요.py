def solution(n):
    a = []
    for r in range(1,n+1):
        if r % 2 != 0:
            a.append(r)
    return a