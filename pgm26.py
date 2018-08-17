n=int(input())
y=list(map(int,input().split(" ")))
y.sort()
for i in range(len(y)):
    if i==len(y)-1:
        print(y[i])
        break
    print(y[i],end=" ")
    
    

    
