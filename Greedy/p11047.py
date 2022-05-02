import sys

nk= list(map(int, sys.stdin.readline().rstrip().split()))
k=nk[1]
count=0
money=list()
for i in range(nk[0]):
  money.append(int(sys.stdin.readline().rstrip()))
money.sort(reverse=True)
for i in money:
  n=k//i
  count+=n
  k%=i
  
 
print(count)