for input in [*open(0)][:-1]:
    a,b=input.split()
    h1,m1=map(int,a.split(":"))
    h2,m2=map(int,b.split(":"))
    m1+=m2
    h1=h1+h2+m1//60
    d=h1//24
    print(f"{h1%24:02}:{m1%60:02}",f"+{d}"if d else "")
    