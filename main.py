import sys

n=int(sys.stdin.readline().rstrip())
a=[0]*10001
for i in range(n):
    a[int(sys.stdin.readline().rstrip())]+=1
 
for i in range(n):
    if a[i]!=0:
        for j in range(a[i]):
            print(i)