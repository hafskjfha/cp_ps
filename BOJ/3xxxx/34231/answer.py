def main():
    n=int(input())
    board=[[*map(int,input().split())]for _ in range(n)]
    ans=0
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(x1,n):
                for y2 in range(y1,n):
                    ans+=check(board,x1,y1,x2,y2)
    print(ans)

def check(board,sx,sy,ex,ey):
    nums=set()
    for i in range(sx,ex+1):
        for j in range(sy,ey+1):
            num=board[j][i]
            if num in nums:
                return 0
            nums.add(num)
    for k in range(1,(abs(sx-ex)+1)*(abs(sy-ey)+1)+1):
        if k not in nums:
            return 0
    return 1
    
main()