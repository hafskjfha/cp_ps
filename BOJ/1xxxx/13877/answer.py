for t,n in [input().split()for _ in range(int(input()))]:
    try:
        print(t,int(n,8),int(n),int(n,16))
    except Exception:
        print(t,0,int(n),int(n,16))