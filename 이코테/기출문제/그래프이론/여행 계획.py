# 10~
# 양방향
# 서로소 집합.. -> 크루스칼?

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
n, m = map(int, input().split()) # 여행지의 수(노드), 계획 도시의 수

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# graph = []
for i in range(n):
    # graph.append(list(map(int, input().split()))) # 2차원 리스트
    graph = list(map(int, input().split())) # (!!!중요) 2차원 리스트를 따로 만들지 말고, 하나 받을 때마다 union을 하자!!!
    for j in range(n):
        if graph[j] == 1:
            union_parent(parent, i + 1, j + 1)

# for i in range(m):
locations = list(map(int, input().split()))
# locations.append(map(int, input().split()))

result = True
for i in range(m - 1):
    if find_parent(parent, locations[i]) != find_parent(parent, locations[i + 1]):
        result = False

if result:
    print("YES")
else:
    print("NO")
###############################################
# 처음에는 크루스칼이라고 생각했는데, 그냥 부모가 같은지만 확인해주는 것이므로(따로 cost 값이 있는게 아니라) 서로소 집합 문제다!
# 2차원 리스트를 만드는데 고생하지 말고, 바로바로 union을 돌리자!
# 빈 배열 선언 후 append할 필요 없이 바로 한번에 list로 선언하며 초기화해주면 됨!(34번쨰 줄)



# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
############################################
