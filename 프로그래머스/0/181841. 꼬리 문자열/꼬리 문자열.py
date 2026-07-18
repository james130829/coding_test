def solution(str_list, ex):
    a = ''
    for b in str_list:
        if ex in b:
            del b
        else:
            a += b
    return a