tym1=list(map(int,input().split(" ")))
tym2=list(map(int,input().split(" ")))
for i in range(0,2):
    if tym1[i]>tym2[i]:
        res=tym1[i]-tym2[i]
    else:
        res=tym2[i]-tym1[i]
    if i==1:
        print(res)
        break
    print(res,end=" ")
