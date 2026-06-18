def main():
    input=open(0).readline
    n,m=map(int,input().split())
    a=[x for x in map(int,input().split())if x<=m]
    
    if not a: return print(-1)
    
    ans=max(a)
    for i in range(m.bit_length()):
        if (m>>i)&1:
            temp=temp2=0
            for x in a:
                #print(bin((m>>(i+1))),bin((x>>(i+1))),(x>>i)&1,x)
                if ((m>>(i+1))|(x>>(i+1)))==m>>(i+1) and ((x>>i)&1)==0:
                    temp|=x
                if x&m==x: 
                    temp2|=x
            ans=max(ans,temp,temp2)
            #print(temp)
    print(ans)
    
    
    


main()