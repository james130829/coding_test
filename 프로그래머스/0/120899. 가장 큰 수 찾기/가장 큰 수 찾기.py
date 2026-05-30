def solution(array):
    a = []
    for m in array:
        a.append(m)
        a.sort(reverse = True)
    b = []
    c = 0
    b.append(a[0])
    for z in array:
        if b[0] == z:
            break
        if b[0]!=z:
            c += 1
    b.append(c)
    return b