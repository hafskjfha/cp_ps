def prefix_sum_2d(mat,n,m):
    psum=[[0]*m for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            psum[i][j] = mat[i-1][j-1]+psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]
    return psum

# for x1,y1,x2,y2 in A:
# 	an = psum[x2][y2]  + psum[x1 -1][y1 -1] - psum[x2][y1 - 1] - psum[x1 - 1][y2]
