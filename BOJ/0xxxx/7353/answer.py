def main():
    input=open(0).readline
    fs,bs,now=[],[],'http://www.acm.org/'
    while 1:
        s=input().strip()
        if not s:continue
        c,*u=s.split()
        if c=='QUIT':break
        if c=='BACK':
            if bs:
                fs.append(now)
                now=bs.pop()
                print(now)
            else:
                print('Ignored')
        elif c=='FORWARD':
            if fs:
                bs.append(now)
                now=fs.pop()
                print(now)
            else:
                print('Ignored')
        elif c=='VISIT':
            bs.append(now)
            now=u[0]
            fs=[]
            print(now)
main()