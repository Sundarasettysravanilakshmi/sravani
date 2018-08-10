r=int(input())
rev=0
temp=r
while(r>0):
	    val=r%10
	    rev=rev*10+val
	    r=r//10
if(temp==rev):
	                   print("yes")
else:
	                   print("no")

	         
