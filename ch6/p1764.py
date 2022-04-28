import sys

n=list(map(int,sys.stdin.readline().rstrip().split()))
dic={}
count=0
for i in range(sum(n)):
  name=sys.stdin.readline().rstrip()
  try:       
    dic[name]+=1
    count+=1
  except:
    dic[name]=1

print(count)
for i in sorted(dic.keys()):
  if dic[i] != 1:
    print(i)