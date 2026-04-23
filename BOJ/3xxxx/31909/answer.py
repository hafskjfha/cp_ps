def main():
    input()
    t={(1<<i)+(1<<j):(i,j)for i in range(8)for j in range(i+1,8)}
    keys={i:i for i in range(8)}
    for x in map(int,input().split()):
        if x in t:
            i,j=t[x]
            keys[i],keys[j]=keys[j],keys[i]
    print(keys[int(input())])
main()