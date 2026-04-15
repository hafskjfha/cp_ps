def main():
    fa=[1,1]
    for i in range(2,31):
        fa.append(fa[i-1]*i)
    for i in [*open(0)][1:]:
        n,m=map(int,i.split())
        print(fa[m]//(fa[n]*(fa[m-n])))
main()