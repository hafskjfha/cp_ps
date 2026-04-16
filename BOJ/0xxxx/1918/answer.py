def main():
    infix_notation=input()
    stack=[]
    result=[]
    property_operator={'+':2,'-':2,'*':3,'/':3,'(':1,')':1,'^':4}
    for token in infix_notation:
        if token.isalnum():
            result.append(token)
        else:
            if token=='(':
                stack.append(token)
            elif token==')':
                while stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and ((token != '^' and property_operator[stack[-1]]>=property_operator[token]) or (token =='^' and property_operator[stack[-1]]>property_operator[token])):
                    result.append(stack.pop())
                stack.append(token)
    while stack:
        result.append(stack.pop())
    print(''.join(result))
            
main()