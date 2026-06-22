def main():
    input=open(0).readline
    n=int(input())
    st=input()
    
    if st.count('6')<=n//2:
        print('7'*st.count('7'))
    else:
        print('6'*st.count('6'))
        
    
    
    
    


main()