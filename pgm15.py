s,p=input().split()
s,p=int(s),int(p)
k=" "
for i in range(s+1,p):
    if(i%2==0):
        if i<2:
            k=" "
        else:k=" "
        print(i,end=k)
                
