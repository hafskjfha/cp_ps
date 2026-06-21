def main():
    input=open(0).readline
    n,c=input().split()
    for _ in range(int(n)):
        if input().strip()[ord(c)-65]=='o':return print("Yes")
    print("No")
    


main()