def main():
    n,m=map(int,input().split())
    board=[[*input()]for _ in range(n)]
    ans=0
    for x in range(m):
        for y in range(n):
            if board[y][x]=='F':
                for dx1,dy1,dx2,dy2 in [(x+1,y,x+2,y),(x-1,y,x-2,y),(x,y+1,x,y+2),(x,y-1,x,y-2),(x+1,y+1,x+2,y+2),(x+1,y-1,x+2,y-2),(x-1,y-1,x-2,y-2),(x-1,y+1,x-2,y+2)]:
                    if 0<=dx1<m and 0<=dx2<m and 0<=dy1<n and 0<=dy2<n and board[dy1][dx1]=='O' and board[dy2][dx2]=='X':
                        ans+=1
                
    print(ans)

main()