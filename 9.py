i=2
while i<=100:
    f=True
    j=2
    while f and j<i:
        if not i%j: f=False
        j+=1
    if f: print(i,end=' ')
    i+=1
