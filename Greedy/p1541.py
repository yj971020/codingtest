n=str(input())
m=n.split('-')
ans=list()
for i in m:
 ans.append(sum(list(map(int,i.split('+'))))) #-로 나눠진 부분의 각 합을 ans 에 저장
  
print(ans[0]-sum(ans[1:])) # 처음부분 - 나머지