# 55분~
# 무방향, 최소 거리 그래프.. -> 크루스칼
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
n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []

# 초기화
for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 정렬
edges.sort()

result = 0
last = 0
# 크루스칼 알고리즘
for edge in edges:
    cost, a, b = edge
    # 사이클이 존재하지 않는다면
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
############################
# [오답]
## 문제를 읽어보면,(마을 2개 ->) 전체 그래프에서 '2개'의 최소 신장 트리를 만들어야 한다.
## 따라서 최소 신장 트리를 구성하는 간선 중에서가정 비용이 큰 간선을 제거하면, 최소 신장 트리가 2개의 부분 그래프로 나누어진다!!!
### 가장 비용이 큰 간선이 마지막(last)인 이유는 오름차순 정렬을 해놓았기 때문!



