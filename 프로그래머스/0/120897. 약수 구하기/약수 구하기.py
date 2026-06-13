def solution(n):
    answer = []
    a = 1
    for m in range(1,n+1):
        if n % m == 0:
            answer.append(m)
    return answer