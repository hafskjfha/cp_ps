def main():
    input=open(0).readline
    s=input().strip()
    for c in s:
        if '0'<=c<='9':
            print(c,end="")

main()