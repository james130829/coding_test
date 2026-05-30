def solution(s1, s2):
    a = 0
    for s in s1:
        for z in s2:
            if s == z:
                a += 1
    return a