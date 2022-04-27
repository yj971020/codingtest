import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
  arr.append(int(sys.stdin.readline()))
count=[0]*(max(arr)+1)

for i in range(len(arr)):
  count[arr[i]]+=1
for i in range(len(count)):
    for j in range(count[i]):
      print(i,end="\n")
   