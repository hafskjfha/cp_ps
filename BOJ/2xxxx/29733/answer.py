def main():
    input=open(0).readline
    r,c,h=map(int,input().split())
    board=[[input().strip()for _ in range(r)]for _ in range(h)]
    count=[[[0]*c for _ in range(r)]for _ in range(h)]
    for z in range(h):
        for y in range(r):
            for x in range(c):
                if board[z][y][x]=='*':
                    count[z][y][x]='*'
                    marking(r,c,h,count,x,y,z)
    for zz in count:
        for yy in zz:
            print(''.join(map(str,yy)))

def marking(r,c,h,count,x,y,z):
    for nz in (z-1,z,z+1):
        if 0<=nz<h:
            for nx,ny in ((x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)):
                if 0<=nx<c and 0<=ny<r and count[nz][ny][nx]!='*':
                    count[nz][ny][nx]=(count[nz][ny][nx]+1)%10
            if nz!=z and count[nz][y][x]!='*':
                count[nz][y][x]=(count[nz][y][x]+1)%10
main()