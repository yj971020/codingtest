n=int(input())
dic={}
for i in range(n):
  word=str(input())
  dic[word]= len(word)

answer=sorted(dic.items(), key= lambda x:(x[1],x[0]))

for i in range(len(answer)):
  print(answer[i][0])
  