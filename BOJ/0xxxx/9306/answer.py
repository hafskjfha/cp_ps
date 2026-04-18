p=[*map(str.strip,[*open(0)][1:])]
print('\n'.join([f'Case {i+1}: '+', '.join(p[i*2:i*2+2][::-1])for i in range(len(p)//2)]))