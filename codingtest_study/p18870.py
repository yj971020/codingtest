import sys

n=int(sys.stdin.readline().rstrip())
xi1=list(map(int,sys.stdin.readline().rstrip().split()))

xi=list(sorted(set(xi1)))
dic=dict()
for i in range(len(xi)):
  dic[xi[i]]=i

for i in xi1:
  print(dic[i],end=' ')