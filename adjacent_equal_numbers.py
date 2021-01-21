def gfunc(lis):
    for i in range(0,len(lis)-1):
        if lis[i] == 3 and lis[i+1] == 3:
            return True
    return False