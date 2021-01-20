def efunc(text):
    xox = text.split()
    revi = xox[::-1]
    return ' '.join(revi)

result = efunc('he is a good guy')
print(result)