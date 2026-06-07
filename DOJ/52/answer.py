def main():
    input=open(0).readline
    n=int(input())
    s=input().strip()
    gc,sc,hc=0,0,0
    for c in s:
        if c=="G":gc+=1
        elif c=="S":sc+=1
        elif c=="H":hc+=1
    
    print(min(gc,sc//2,hc))
    
    
main()