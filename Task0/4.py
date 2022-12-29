from functools import reduce

def generate_AP(a1,d,n):
    global i
    AP_series = []
    for i in range(n,0,-1):
       s = a1+(n-i)*d 
       AP_series.append(s)

    return AP_series

test_cases = int(input())
x,y,z = input().split()
a1 = int(x)
d = int(y)
n = int(z)
AP_series = generate_AP(a1,d,n)

i=0
for i in range(0,n):
    if(i == (n-1)):
        print(AP_series[i])
    else:
        print(AP_series[i], end=" ")

sqr_AP_series = []
sqr_AP_series = list(map(lambda j: j*j, AP_series))
i = 0
for i in range(0,n):
    if(i == (n-1)):
        print(sqr_AP_series[i])
    else:
        print(sqr_AP_series[i], end=" ")

i=0
sum_sqr_AP_series = reduce((lambda i,j:i+j),sqr_AP_series)
print(sum_sqr_AP_series, end="")