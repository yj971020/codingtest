a=[i for i in range(20)]
print(a)
a="abcedfsfd"
print(a[2:4])
print(a[3:7])

data=dict()

#튜플
data['사과']=1
data['오렌지']='orange'
data['코코넛']=3
print(data)

#set 집합자료형
#초기화 방법1
data1={11,1,1,2,3,4,4,5}
print(data1) #중복 안됨

#초기화 방법2
data1=set([1,2,3,4,4])
data1.update([3,4,4,5,6,7])
print(data1)
data1.remove

i = 1
result = 0
#while 문
while(i<=9):
	if i % 2 == 1 :
		result += i
	i += 1

print(result)
	

#for 문
result =0 
for i in range(10) :
	result += i
  
print(result)

#함수
def add(a,b):
    return a+b

print(add(3,7))

#람다표현식
print((lambda a, b : a+b)(3,7))
