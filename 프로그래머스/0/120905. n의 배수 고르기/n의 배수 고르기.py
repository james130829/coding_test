def solution(n, numlist):
    b = []
    for m in numlist:
        if m % n == 0:
            b.append(m)
    return b