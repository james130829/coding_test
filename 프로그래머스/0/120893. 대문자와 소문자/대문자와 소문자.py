def solution(my_string):
    a = ""
    for m in my_string:
        if m.isupper():
            a += m.lower()
        if m.islower():
            a += m.upper()
    return a