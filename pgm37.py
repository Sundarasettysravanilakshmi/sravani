inp=list(map(int,input().split(" ")))
out=inp[::-1]
for i in range(len(out)):
    if i==len(out)-1:
        print(out[i])
        break
    else:
        print(out[i],end=" ")
