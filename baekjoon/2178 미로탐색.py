# 10분~
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False

dfs(0,0)