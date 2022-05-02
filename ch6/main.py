n=str(input())
m=n.split('-')
ans=list()
for i in m:
  ans.append(sum(list(map(int,i.split('+')))))

print(ans[0]-sum(ans[1:]))