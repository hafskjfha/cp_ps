def main():
    i=1
    for p in[*open(0)][:-1]:
        r,w,l=map(int,p.split())
        print(f'Pizza {i} {["does not fit","fits"][(w**2+l**2)**0.5<=r*2]} on the table.')
        i+=1      
main()