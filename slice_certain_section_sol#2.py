def func(mylist):
    total = 0
    add = True
    for i in mylist:
            if i == 6:
                add = False
            if add == True:
                total += i
            if i == 9:
                add = True


    return total
lt=[2,3,4,6,8,10,9,1,2,6,5,4,9,3]

print(func(lt))