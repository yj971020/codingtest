def solution(A):
    turned_on=[0]*5
    count=0
    for i in range(len(A)):
        index=A[i]-1 #1번 전구 정보를 배열의 0 인덱스에 저장
        turned_on[index]=1
        if i>=index: # on_count>= number of bulb
            for j in range(i+1):
                if turned_on[j]!=1:
                    print(j,"J")
                    break                
            count+=1   
    return count        
        
print(solution([2,1,3,5,4]))       

    