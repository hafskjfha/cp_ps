def main():
    s = [*open(0)][1].strip()
    a = []
    p = ["Adrian","Bruno", "Goran"]
    def sc(s,t):
        o = 0
        for i in range(len(s)):
          if s[i] == t[i%len(t)]:
              o+=1
        return o
    for k in (["A","B","C"],["B","A","B","C"],["C","C","A","A","B","B"]):
        a.append(sc(s,k))
    print(max(a))
    for i in range(3):
        if a[i]==max(a):
            print(p[i])
main()