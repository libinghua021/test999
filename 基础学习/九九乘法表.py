for i in range(1,10):
    line = ''
    for j in range(1,10):
        if j >= i:
             line += "{}*{}={:<2} ".format(i,j,i*j)
        else:
            line += '       '
    print(line)