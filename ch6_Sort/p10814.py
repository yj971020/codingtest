import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
for i in range(n):
  arr.append(sys.stdin.readline().rstrip().split())
  arr[i][0]=int(arr[i][0])

arr.sort(key=lambda x: x[0])
for i,j in arr:
  print(i,j)

