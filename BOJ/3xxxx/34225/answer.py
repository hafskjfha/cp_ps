def main():
    input()
    max_a=None
    suma=0
    ans=[]
    max_sum=0
    idx=0
    ridx=0
    for i,a in sorted(enumerate(map(int,input().split()),1),key=lambda x:-x[1]):
        if max_a==None:
            max_a=a
            suma=a
            max_sum=a*3
        else:
            t=max_a+2*a+suma
            if max_sum<t:
                max_sum=t
                ridx=idx
            suma+=a
        ans.append(i)
        idx+=1
    print(len(ans[:ridx+1]))
    print(*ans[:ridx+1])
main()

