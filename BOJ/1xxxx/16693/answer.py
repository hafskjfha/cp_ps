a,p1=map(int,input().split())
r,p2=map(int,input().split())
print("Whole pizza" if (r*r*3.14159265358979323846)/p2 > a/p1 else "Slice of pizza")