def func1(ulist):
    compare = [0,0,7,'x']
    for i in ulist:
        if i == compare[0]:
            compare.pop(0)
    return len(compare) == 1
ulist=[1,2,0,0,7,8,9]
print(func1(ulist))