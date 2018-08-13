x,y=input().split()
x,y=int(x),int(y)
count=0
for i in range(x+1,y):
    if(i%2!=0):
        if i<y-2:
            k=" "
        else:k=""
        print(i,end=k)
