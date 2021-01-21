def func(a,b,c):
    x = a+b+c
    if  x <= 21:
        return x
    elif 11 in [a,b,c] and x-10 <= 21:
        return x-10
    else:
        return 'BUST'