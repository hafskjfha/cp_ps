def main():
    a=input()
    b=input()
    dp=lcs(a,b)
    x=dp[-1][-1]
    print(x)
    if x:print(traceback(dp,a,b))

def lcs(a,b):
    lena,lenb=len(a),len(b)
    dp=[[0]*(lena+1)for _ in range(lenb+1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i]==b[j]:
                dp[j+1][i+1]=dp[j][i]+1
            else:
                dp[j+1][i+1]=max(dp[j][i+1],dp[j+1][i])
    return dp

def traceback(dp,a,b):
    pi,pj=len(a),len(b)
    ans=[]
    while pi>0 and pj>0:
        if a[pi-1]==b[pj-1]:
            ans.append(a[pi-1])
            pi-=1
            pj-=1
        else:
            if dp[pj-1][pi]>dp[pj][pi-1]:pj-=1
            else: pi-=1

    return ''.join(ans[::-1])
main()