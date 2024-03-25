# ~1
# 5
# 2 3 1 2 2

n = int(input())
fear_levels = list(map(int, input().split()))
# for i in range(n):

# 정렬
fear_levels.sort() # 1 2 2 2 3

group_count = 0 # 그룹 수
count = 0 # 현재 그룹에 포함된 모함가 수

for fear in fear_levels:
     count += 1
     if count >= fear:
         group_count += 1
         count = 0

print(group_count)

############################################
# 변수명은 딱 보면 뭐인지 알 수 있도록 짓기
# 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성