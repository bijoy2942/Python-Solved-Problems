def myfunc(string):
    empty = []
    for i in range(len(string)):
        if i % 2 == 0:
            empty.append(string[i].lower())
        else:
            empty.append(string[i].upper())
    return ''.join(empty)

print('result', myfunc('MeTaDaTa'))