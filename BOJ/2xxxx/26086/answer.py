def main():
    from collections import deque
    input=open(0).readline
    n,q,k=map(int,input().split())
    dq=deque()
    ss,se,sr=None,None,False
    is_reversed=False
    for _ in range(q):
        c,*x=map(int,input().split())
        if c==0:
            if is_reversed:
                if ss!=None: ss+=1;se+=1
                dq.appendleft(x[0])
            else: 
                dq.append(x[0])
        elif c==1:
            ss,se,sr=0,len(dq),is_reversed
        else:
            is_reversed=not is_reversed
    dq=list(dq)
    if ss!=None:
        dq[ss:se]=sorted(dq[ss:se],reverse=not sr)
    print([dq[-k],dq[k-1]][is_reversed])
main()