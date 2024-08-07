# 38~

# begin -> target
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return
# 변환할 수 없는 경우에는 0를 return

# hit / cog
# ["hot","dot","dog","lot","log","cog"]라면 
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# cog를 배열로 만들고, 하나만 다른게 있는지 words에서 확인
# bfs

# 1. 배열 안에 target 값 유무 확인
# 2. 하나만 다른게 있으면 큐에 넣기
# 3. 

from collections import deque

def solution(begin, target, words):
    visited = [False] * len(words)
    
    # 1.
    if target not in words:
        return 0
    
    def bfs(start):
        q = deque([(start, 0)]) # 2. 시작 단어와 0으로 초기화한 단계
        while q:
            now, step = q.popleft()
            # count = 0 # 여기에 선언하지 말고
            if now == target:
                return step
            
            # 3.      
            for j, word in enumerate(words):
                count = 0 # 여기에 선언해주면
                
                for i in range(len(now)):
                    if visited[j]==False and now[i] != word[i]:
                        count += 1
                
                if count == 1:
                    q.append((word, step + 1))
                    visited[j] = True
                    
                # count = 0 # 여기서 또 초기화해줄 필요가 없다!
               
    return bfs(begin) # (후)return을 해준다.

    # cog
    # (O) dot -> dog
    # (X) dot -> lot
    # 