def solution(n):
    answer = 0
    for a in range(0,n+1):
        if n % 2 == 0:
            if a % 2 == 0:
                answer += a * a
        if n % 2 != 0:
            if a % 2 != 0:
                answer += a
    return answer