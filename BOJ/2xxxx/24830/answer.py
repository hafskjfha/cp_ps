def main():
    r=1
    for i in [*open(0)][1:]:
        a,p,b=i.split()
        a,b=map(int,[a,b])
        if p=="+":
            r=a+b-r
            print(r)

        elif p=="-":
            r=(a-b)*r
            print(r)

        elif p=="*":
            r=(a*b)**2
            print(r)

        else:
            if a&1:
                a+=1
            r=a//2
            print(r)
main()