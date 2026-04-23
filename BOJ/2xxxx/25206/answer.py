def main():
    g={'A+':4.5,'A0':4,'B+':3.5,'B0':3,'C+':2.5,'C0':2,'D+':1.5,'D0':1,'F':0}
    s=0
    j=0
    for _,h,i in map(str.split,open(0)):
        if i=='P':continue
        s+=float(h)*g[i]
        j+=int(float(h))
    print(s/j)
main()