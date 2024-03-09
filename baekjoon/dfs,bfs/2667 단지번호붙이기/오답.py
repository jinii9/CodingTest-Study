# 37분~
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y, count):
    if x<0 or y<0 or x>=n or y>=n:
        return False, count
    if graph[x][y] == 0:
        return False, count

    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x-1, y, count)
        dfs(x+1, y, count)
        dfs(x, y-1, count)
        dfs(x, y+1, count)
        return True, count

    return False, count


result = 0
arr = []
for i in range(n):
    for j in range(n):
        check, count = dfs(i, j, 0)
        if check == True:
            result += 1
            arr.append(count)

print(result)
arr.sort()
for i in arr:
    print(i)

########################################################
# dfs(x-1, y, count)와 같이 count 값을 늘려가면 안되는 이유
## dfs 함수가 호출된 후 count 값이 1 증가 했다고 가정했을 때, dfs 함수가 종료되고 상위 함수로 돌아갈 때는 count 값이 그때 당시의 count 값으로 될아가게 된다(감소된다).
## ex) (0, 0)에서 dfs를 호출하면 count = 1이 된다. 그리고 (0, 1)에서 dfs를 호출하면 count = 2가 된다. 하지만 이 상태에서 (0, 1)에서의 dfs 호출이 종료되면 count 값은 다시 1로 돌아간다.
