def sol(n,k,arr):
    answer=[]
    count=[k]*n #array of left space in each floor
    left=[i for i in range(n)]  #array of left floor
    
    
    for i in arr:
        index=i-1 #index = floor-1
        while True:    
            if count[index]!=0:
                answer.append(index+1)
                count[index]-=1
                if count[index]==0:
                    left.remove(index)
                break
            else:
                temp=[abs(i-index) for i in left]
                index=left[temp.index(min(temp))]
            
    return answer
    
sol(5,2,[3,1,2,2,4,3,1,1,5,2])
    