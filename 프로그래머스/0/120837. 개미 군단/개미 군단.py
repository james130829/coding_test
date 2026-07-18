def solution(hp):
    z = 0
    a=5
    b=3
    c=1
    if hp > 0:
        z += hp // a
        hp = hp % a
    if hp > 0:
        z += hp // b
        hp = hp % b
    if hp > 0:
        z += hp // c
        hp = hp % c
    return z