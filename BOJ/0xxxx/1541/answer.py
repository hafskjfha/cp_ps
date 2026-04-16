def main():
    s=input()
    a=s.split('-')
    r=sum(map(int,a[0].split('+')))
    for ns in a[1:]:
        r-=sum(map(int,ns.split('+')))
    print(r)
main()