s=int(raw_input())
p=int(raw_input())
 
for n in range(s,p):
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum =sum+ digit ** 3
       temp /= 10
 
   if n == sum:
       print(n)
