def solution(rsp):
    a = ''
    for r in rsp:
        if r == "2":
            a += "0"
        elif r == "0":
            a += "5"
        elif r == "5":
            a += "2"
    return a