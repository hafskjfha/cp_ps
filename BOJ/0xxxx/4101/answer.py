for k in [*open(0)][:-1]:
    a,b=map(int,k.split())
    print("YNeos"[not a>b::2])