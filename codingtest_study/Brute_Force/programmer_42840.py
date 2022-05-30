#나의 풀이
def solution(answers):
    answer = []
    scores={1:0,2:0,3:0}
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==p1[i%len(p1)]:
            scores[1]+=1
        if answers[i]==p2[i%len(p2)]:
            scores[2]+=1
        if answers[i]==p3[i%len(p3)]:
            scores[3]+=1
            
    for i in scores:
        if max(scores.values())==scores[i]:
            answer.append(i)
        
    return answer