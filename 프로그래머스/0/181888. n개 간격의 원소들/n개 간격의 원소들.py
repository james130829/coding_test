def solution(num_list, n):
    a = []
    c = 0
    for b in num_list:
        if c % n == 0:
            a.append(b)
        c+= 1
    return a