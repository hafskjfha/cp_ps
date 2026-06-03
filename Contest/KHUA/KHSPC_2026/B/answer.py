def main():
    input=open(0).readline
    for _ in range(int(input())):
        s=input().strip()
        for cc in s.split(' - '):
            h,m=map(int,cc.split(':'))
            if 60<=h*60+m<=779:
                pass
            else:
                return print("KHU Library")
    print("check the time again")

main()