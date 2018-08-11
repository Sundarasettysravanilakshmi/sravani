num = int(input())
 
for p in range(2, int(num/2)):
    if num % p  == 0:
        print("no")
        break
else:
        print("yes")
