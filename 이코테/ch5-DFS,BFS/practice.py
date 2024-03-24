n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global count
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y] == 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False

result = 0
count_data = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j) == True:
            result += 1
            count_data.append(count)

print(result)
count_data.sort()
for i in count_data:
    print(i)