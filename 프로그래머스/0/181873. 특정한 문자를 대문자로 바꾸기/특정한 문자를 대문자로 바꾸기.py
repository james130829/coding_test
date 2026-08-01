def solution(my_string, alp):
    a = ''
    for m in my_string:
        if m == alp:
            a += m.upper()
        elif m != alp:
            a += m
    return a