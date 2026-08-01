def solution(order):
    a = 0
    o = str(order)
    for i in o:
        if i == "3":
            a += 1
        if i == "6":
            a += 1
        if i == "9":
            a += 1
    return a