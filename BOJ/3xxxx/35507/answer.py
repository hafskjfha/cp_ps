def solve(n,ps):
    a=b=c=p=0
    for x,y,z,k in ps:
        if x>a:
            p+=x-a
            a=x
        if y>b:
            p+=y-b
            b=y
        if z>c:
            p+=z-c
            c=z
        if p+1>k:return "NO"
        p+=1
    return "YES"

def main():
    input=open(0).readline
    for _ in range(int(input())):
        n=int(input())
        ps=[[*map(int,input().split())]for _ in range(n)]
        #print(ps)
        print(solve(n,ps))
            

main()