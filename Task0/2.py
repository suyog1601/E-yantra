import math as m
def compute_distance(x1,y1,x2,y2):
    distance = m.sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
    return distance

test_cases = int(input())
i = 0
z = []
for i in range(0,test_cases):
    a1,b1,a2,b2 = input().split()
    x1 = int(a1)
    y1 = int(b1)
    x2 = int(a2)
    y2 = int(b2)
    dist = compute_distance(x1,y1,x2,y2)
    z.append(dist)

i = 0
t = test_cases-1
while(i<t):
    print("Distance: %.2f" %z[i])
    i = i+1
print("Distance: %.2f" %z[i], end="")
