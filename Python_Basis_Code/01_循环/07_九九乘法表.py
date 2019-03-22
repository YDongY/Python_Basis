i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (j, i, i * j), end='\t')
        j += 1
    i += 1
    print('')
