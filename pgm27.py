n=input()
try:
    float(n)
    print("Yes")
except ValueError:
    print("No")
