for _ in range(int(input())):
    input()
    c=[0,0]
    for x in map(int,input().split()):c[x%2]+=1
    if (c[0]%2==1 and c[0]>c[1])or(c[1]%2==1 and c[0]<c[1]):
        print('amsminn')
    else:
        print('heeda0528')