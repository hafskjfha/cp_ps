input=open(0).readline
for _ in range(int(input())):
    b=[[*input().strip()]for _ in range(3)]
    t=input().strip()
    for i in range(3):
        p,px,py=0,-1,-1
        q,qx,qy=0,-1,-1
        for j in range(3):
            if b[i][j]==t:
                p+=1
            elif b[i][j]=='-':
                px,py=j,i

            if b[j][i]==t:
                q+=1
            elif b[j][i]=='-':
                qx,qy=i,j
        if p==2:
            b[py][px]=t
            break
        elif q==2:
            b[qy][qx]=t
            break
    else:
        p,px,py=0,-1,-1
        q,qx,qy=0,-1,-1
        for i in range(3):
            for j in range(3):
                if i==j:
                    if b[i][j]==t:
                        p+=1
                    elif b[i][j]=='-':
                        px,py=j,i
                if (i,j) in ((0,2),(1,1),(2,0)):
                    if b[i][j]==t:
                        q+=1
                    elif b[i][j]=='-':
                        qx,qy=j,i
        if p==2:
            b[py][px]=t
        elif q==2:
            b[qy][qx]=t
    print(f"Case {_+1}:")
    for f in b:
        print(''.join(f))
                