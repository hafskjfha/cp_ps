def main():
    input=open(0).readline
    for _ in range(int(input())):
        n=int(input())
        for b in range(2,65):
            if k(c(n,b)):
                print(1)
                break
        else:
            print(0)
    
def c(n,b):
    r=[]
    while n:
        n,m=divmod(n,b)
        r=[m]+r
    return r

def k(r):
    return r==r[::-1]

main()