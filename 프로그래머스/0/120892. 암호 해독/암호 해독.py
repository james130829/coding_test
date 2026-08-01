def solution(cipher, code):
    a = 0
    b = ''
    for r in cipher:
        a += 1
        if a % code == 0:
            b += r
    return b