import sys,math

def main():
    input=sys.stdin.readline
    n=int(input())
    s=input().strip()
    
    ans=0
    j=-1
    for i in range(n):
        if s[i] in "67":
            if j==-1:j=i
        else:
            if j!=-1:
                ans+=math.ceil((i-j)/2)
                j=-1
    
    if j!=-1:
        ans+=math.ceil((n-j)/2)
    
    print(ans if ans<=n//2 else -1)


main()