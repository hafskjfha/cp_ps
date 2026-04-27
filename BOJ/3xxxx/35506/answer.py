def solve(n):
    for i in range(2*n):
        print(" "*(2*n-1-i)+"*",end="")
        if i<n:
            print(" "*n+"*"+" "*(2*i+1)+"*"+" "*(4*n+2-(2*n-1-i+1+n+1+2*i+2)))
        else:
            print(" "*(n+2*(i-n)+1)+"*"+" "*(1 + 2*(2*n-i-1))+"*"+" "*(4*n-((2*n-1-i)+n+2*(i-n)+3+2*(2*n-i-1))))
            

def main():
    input=open(0).readline
    solve(int(input()))    
            

main()