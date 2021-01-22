#def func(mylist):
    total = 0
    add = True
    for i in mylist:
        while add:
            if i != 6:
                total = i + total
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total
print(func([1,2,6,7,9,3,5]))#


