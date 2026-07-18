def solution(num_list):
    a = 0
    for n in num_list:
        a += 1
        if n < 0:
            return a - 1
    return -1
