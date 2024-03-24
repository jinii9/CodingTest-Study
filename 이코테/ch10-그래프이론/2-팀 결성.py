# 30분~
n, m = map(int, input().split())
parent =[0] * (n + 1)

## 빼먹질 말 것!!!!!!
for i in range(0, n + 1):
    parent[i] = i

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

for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        # 합치기
        union_parent(parent, a, b)
    elif check == 1:
        # 같은 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1