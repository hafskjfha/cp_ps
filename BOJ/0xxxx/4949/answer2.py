import sys
input = lambda: sys.stdin.readline()

def check(sentence):
    stack = []
    for ch in sentence:
        if (ch == "(" or ch == "["):
            stack.append(ch)
        elif (ch == ")" or ch == "]"):
            if (len(stack) == 0):
                return False
            else:
                left = stack.pop()
                if (ch == ")"):
                    if (left != "("):
                        return False
                elif (ch == "]"):
                    if (left != "["):
                        return False
    if (len(stack) == 0):
        return True
    else:
        return False

while True:
    sen = input()
    if (sen == ".\n"):
        break
    else:
        if check(sen.strip()):
            print("yes")
        else:
            print("no")