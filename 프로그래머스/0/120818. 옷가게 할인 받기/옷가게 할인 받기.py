def solution(price):
    a = 0
    if price >= 100000 and price < 300000:
        return int(price - ((price / 100) * 5))
    elif price >= 300000 and price < 500000:
        return int(price - ((price / 100) * 10))
    elif price >= 500000:
        return int(price - ((price / 100) * 20))
    else:
        return price