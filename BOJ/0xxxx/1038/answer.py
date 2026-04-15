r=[]
def back(arr):
    if arr and arr[-1]==9:
        return
    for i in range(arr[-1]+1 if arr else 0,10):
        arr.append(i)
        r.append(''.join(map(str,arr[::-1])))
        back(arr)
        arr.pop()
back([])
r.sort(key=int)
n=int(input())
print(-1if n>1022 else r[n])