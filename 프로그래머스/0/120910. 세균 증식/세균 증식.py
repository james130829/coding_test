def solution(n, t):
    a = n
    for b in range(0,t+1):
        a = a * 2
    return a / 2