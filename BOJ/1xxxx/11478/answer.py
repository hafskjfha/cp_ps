def main():
    s=input()
    print(len({s[i:j]for i in range(len(s)+1)for j in range(i+1,len(s)+1)}))
main()