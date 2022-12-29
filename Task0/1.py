test_cases = int(input())
 # Write your code from here
i = 0
a = []
for i in range(0,test_cases):
 n = int(input())
 a.append(n)

i = 0
r = 0
for i in range(0,test_cases):
 b = a[i]-1
 c = test_cases-1
 if(i == c):
  for r in range(0,a[i]):
   if(r == 0):
    print(r+3,end="")
   elif(r%2 == 0):
    print(' %d' %(2*r),end="")
   else:
    print(' %d' %(r*r),end="")
 else:
  for r in range(0,a[i]):
   if(r == b):
    if(r == 0):
     print(r+3)
    elif(r%2 == 0):
     print(' %d' %(2*r))
    else:
     print(' %d' %(r*r))
   else:
    if(r == 0):
     print(r+3,end="")
    elif(r%2 == 0):
     print(' %d' %(2*r),end="")
    else:
     print(' %d' %(r*r),end="")


