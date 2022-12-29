test_cases = int(input())
l = int(input())
a = []
a = [int(item) for item in input().split()]
c = l-1
for i in range(c,-1,-1):
    if(i == 0):
        print(a[i])
    else:
        print(a[i], end=" ")
x = 0
for i in range(1,l):
    if(x == 0):
        if(i%3 == 0):
            print(a[i]+3, end="")
            x=x+1
    else:
        if(i%3 == 0):
            print(" %d" %(a[i]+3), end="")
print()
i = 0
x = 0
for i in range(1,l):
    if(x == 0):
        if(i%5 == 0):
            print(a[i]-7, end="")
            x=x+1
    else:
        if(i%5 == 0):
            print(" %d" %(a[i]-7), end="")
print()
print(a[3]+a[4]+a[5]+a[6]+a[7], end = "")
