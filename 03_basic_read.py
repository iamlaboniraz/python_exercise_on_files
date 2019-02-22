with open('03_basic_read.txt') as f:
    for line in f:
        a,b,c=line.split(',')
        print(a,'-',c)
