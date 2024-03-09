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

# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# def dfs(x, y):
#     if x<0 or y<0 or x>=n or y>=n:
#         return False
#     if graph[x][y] == 0:
#         return False
#
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         count = 1 # 현재의 집 카운트
#         count += dfs(x-1, y) or 0 # 집이 있다면, 그 집의 수를 반환하고, 그 수가 count에 더해진다.
#         count += dfs(x+1, y) or 0
#         count += dfs(x, y-1) or 0
#         count += dfs(x, y+1) or 0
#         return count
#
#     return 0
#
#
# result = 0
# arr = []
# for i in range(n):
#     for j in range(n):
#         temp = dfs(i, j)
#         if temp: # True일 때
#             result += 1
#             arr.append(temp)
#
# print(result)
# arr.sort()
# for i in arr:
#     print(i)
