import sys

con=int(sys.stdin.readline().rstrip())
howfar=list(map(int,sys.stdin.readline().rstrip().split()))
oil=list(map(int,sys.stdin.readline().rstrip().split()))

total=0
j=0 #작은 오일값의 인덱스
for i in range(con-1):
  if oil[j]>oil[i]:
    j=i 
  
  total+=oil[j]*howfar[i]

print(total)
  
  