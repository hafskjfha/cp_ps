import bisect
n=int(input())
files=sorted(map(int,input().split()))
print(sum(abs(bisect.bisect_left(files,files[i]*0.9)-i)for i in range(n)))