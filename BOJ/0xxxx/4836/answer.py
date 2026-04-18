for s in open(0):
    l=s.split()
    error=[]
    for i in range(len(l)):
        x=l[i]
        if x=='dip':
            if not((i-1>=0 and l[i-1]=='jiggle') or (i-2>=0 and l[i-2]=='jiggle') or (i+1<len(l) and l[i+1]=='twirl')):
                error.append(1)
                l[i]=x.upper()
    if ' '.join(l[-3:])!='clap stomp clap':error.append(2)
    if 'twirl' in l and 'hop' not in l:error.append(3)
    if l[0]=='jiggle':error.append(4)
    if 'dip' not in s:error.append(5)
    s=' '.join(l)
    if len(error)==0:
        print('form ok:',s)
    elif len(error)==1:
        print(f'form error {error[0]}:',s)
    else:
        print(f'form errors {", ".join(map(str,error[:-1]))} and {error[-1]}:',s)
        
    