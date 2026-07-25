def solution(numbers):
    a = -10000 * 10000
    for x in range(0,len(numbers)):
        for y in range(x+1,len(numbers)):
            if numbers[x] * numbers[y] >= a:
                a = numbers[x] * numbers[y]
    return a