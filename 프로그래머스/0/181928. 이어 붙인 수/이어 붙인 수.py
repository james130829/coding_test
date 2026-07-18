def solution(num_list):
    b = ''
    c = ''
    for a in num_list:
        if a % 2 == 0:
            b += str(a)
        elif a % 2 != 0:
            c += str(a)
    return int(c) + int(b)