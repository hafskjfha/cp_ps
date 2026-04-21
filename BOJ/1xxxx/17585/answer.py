def main():
    n=int(input())
    b=map(lambda x:x=='T',input().split())
    var={chr(65+i):next(b)for i in range(n)}
    stack=[]
    for token in input().split():
        if token.isalpha():stack.append(var[token])
        else:
            if token=='-':stack.append(not stack.pop())
            else:
                v1,v2=stack.pop(),stack.pop()
                if token=='*':
                    stack.append(v1&v2)
                else:
                    stack.append(v1|v2)
    print("FT"[stack[0]])
main()