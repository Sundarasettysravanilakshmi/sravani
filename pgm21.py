N,A,D=map(int,input().split())
sum=0
for s in range(N):
    sum=sum+A
    A=A+D
    s=s+1
print (sum)
