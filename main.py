n=int(input())
array=[]
score={}
for i in range(n):
    array.append(str(input()))
    r= array[i].split()
    score[r[1]]=r[0]
for str in sorted(r).values:
    print(str,end=" ")