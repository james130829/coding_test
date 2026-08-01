def solution(my_string, num1, num2):
    a = my_string[num1]
    b = my_string[num2]
    c = ''
    d = 0
    for m in my_string:
        if d != num1 and d != num2:
            c+=m
        elif d == num1:
            c+=b
        elif d == num2:
            c+=a
        d+=1
    return c