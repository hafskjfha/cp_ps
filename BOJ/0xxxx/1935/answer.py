def main():
    n=int(input())
    postfix_notation=input()
    var={chr(65+i):int(input()) for i in range(n)}
    stack=[]
    for token in postfix_notation:
        if token.isalpha():
            stack.append(token)
        else:
            v1,v2=stack.pop(),stack.pop()
            stack.append(str(eval(str(var.get(v2,v2))+token+str(var.get(v1,v1)))))
    print(f"{float(stack.pop()):.2f}")
main()