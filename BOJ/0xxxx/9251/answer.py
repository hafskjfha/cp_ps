def main():
    a=input()
    b=input()
    dp=lcs(a,b)
    print(dp[-1][-1])

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

main()