def main():
    r=[]
    for sn in map(lambda x:x.strip(), [*open(0)][1:]):
        n=int(sn)
        l=len(sn)
        c=0
        for i in range(l,0,-1):
            k=int("8"*i)
            c+=n//k
            if c>8:
                break
            n%=k
            if n==0:
                break
        
        if n:
            r.append("No")
        else:
            r.append("Yes")
    print("\n".join(r))
main()