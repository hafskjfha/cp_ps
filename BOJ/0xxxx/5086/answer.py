for i in map(str.split,[*open(0)][:-1]):
    x,y=map(int,i)
    if y%x==0:print('factor')
    elif x%y==0:print('multiple')
    else:print('neither')