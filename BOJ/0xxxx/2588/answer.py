a,b=int(input()),int(input())
print(a*(b%10),a*(b-b//100*100-b%10)//10,a*(b//100*100)//100,a*b)