def solution(my_string):
    a = []
    for m in my_string:
        if m.isdigit():
            a.append(int(m))
    return sorted(a)