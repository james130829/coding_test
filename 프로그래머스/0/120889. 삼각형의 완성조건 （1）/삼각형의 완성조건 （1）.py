def solution(sides):
    a = []
    for s in sides:
        a.append(s)
        a.sort()
    if a[2] < a[0]+a[1]:
        return 1
    if a[2] >= a[0]+a[1]:
        return 2