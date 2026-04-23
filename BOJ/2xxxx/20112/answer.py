n=int(input())
b=[input()for _ in " "*n]
for i in range(n):
    for j in range(i+1,n):
        if b[i][j]!=b[j][i]:exit(print("NO"))
print("YES")