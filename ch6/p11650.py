import sys

n=int(sys.stdin.readline().rstrip())
arr=[]

for i in range(n):
  arr.append( list(map(int,sys.stdin.readline().rstrip().split())))

arr.sort(key= lambda x: (x[0],x[1]))
for i, j in arr:
  print(i,j)