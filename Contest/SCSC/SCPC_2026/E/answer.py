def main():
    input=open(0).readline
    for _ in range(int(input())):
        n=int(input())
        s=input().strip()
        ans=[]
        for i in range(n):
            j=(i+1)%n
            k=(i-1)%n
            l=(i+2)%n
            m=(i-2)%n
            if (s[i]!=s[j] and s[i]!=s[k]) or (s[j]==s[l]) or (s[k]==s[m]):
                ans.append('1')
            else:
                ans.append('2')
        print(' '.join(ans))
    

main()