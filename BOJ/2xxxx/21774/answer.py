def main():
    from bisect import bisect_left,bisect_right
    import sys
    input=sys.stdin.readline
    n,q=map(int,input().split())
    logs=[[],[],[],[],[],[]]
    result=[]
    for _ in range(n):
        date,lv=input().strip().split('#')
        logs[int(lv)-1].append(to_sec(date))
    
    for _ in range(q):
        start,end,llv=input().strip().split('#')
        ssec,esec=to_sec(start),to_sec(end)
        ans=0
        for lv in range(int(llv)-1,6):
            si,ei=bisect_left(logs[lv],ssec),bisect_right(logs[lv],esec)
            ans+=ei-si
        result.append(str(ans))
    print('\n'.join(result))

def to_sec(s):
    y,m,d=map(int,s[0:10].split('-'))
    h,mi,se=map(int,s[11:].split(':'))
    return (y-2000)*12*31*24*3600+(m-1)*31*24*3600+(d-1)*24*3600+h*3600+mi*60+se

main()