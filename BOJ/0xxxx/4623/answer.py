for i in [*open(0)][:-1]:
    a,b,c,d=map(int,i.split())
    if (a>b and c<d)or(a<b and c>d):a,b=b,a
    print(f'{min(int((min(c/a,d/b))*100),100)}%')