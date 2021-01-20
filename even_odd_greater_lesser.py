def afunc(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            result = a
        else:
            result = b
        # return min(a,b)
    else:
        # return max(a,b)
        if a > b:
            result = a
        else:
            result = b
    return result