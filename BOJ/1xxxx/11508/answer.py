def main():
    input=open(0).readline
    a=sorted([int(input())for _ in range(int(input()))],key=lambda x:-x)
    cost=0
    for i in range(0,len(a),3):
        b=a[i:i+3]
        cost+=sum(b)-min(b) if len(b)==3 else sum(b)
    print(cost)
main()