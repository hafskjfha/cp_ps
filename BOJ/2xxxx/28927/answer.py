a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
f,t=a*3+b*20+c*120,x*3+y*20+z*120
print('Draw'if f==t else'MMaexl'[f<t::2])