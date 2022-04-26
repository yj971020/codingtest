n=int(input())
a=list(map(int,input().split()))

a.sort()
b=[a[0]]

for i in range(1,n):
   b.append(b[i-1]+a[i])
    
print(sum(b))    