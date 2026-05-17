def main():
    input=open(0).readline
    for _ in range(int(input())):
        s=input().strip()
        if len(s)%2==1 or "SSCSC" in s or "SCCSC" in s or "SCSSC" in s or "SCSCC" in s:
            print("Terra")
        else:
            print("Lulu")

main()