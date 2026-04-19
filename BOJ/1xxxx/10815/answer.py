def main():
    input=open(0).readline
    input()
    card={x:"1"for x in map(int,input().split())}
    input()
    print(' '.join([card.get(x,"0")for x in map(int,input().split())]))
main()