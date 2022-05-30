from collections import deque

def solution(priorities, location):
  answer=0
  q = deque(priorities)
  for i in range(len(priorities)):
    v=q.popleft()
    if v<=min(q):
      answer+=1
    else:
      q.append(v)
  return answer

print(solution([1,1,9,1,1,1],0))