def solution(tickets):
    # 일반 딕셔너리 사용
    graph = {}

    # 그래프 생성 및 알파벳 순으로 정렬
    for a, b in tickets:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    print("graph", graph)
    # 각 리스트를 알파벳 순으로 정렬
    for key in graph:
        print(graph[key])
        graph[key].sort()
    print("graph", graph)

    route = []

    def dfs(airport):  # airport : 현재 공항의 이름
        while airport in graph and graph[airport]:  # 출발 공항이 그래프에 존재하고, 도착할 공항이 남아 있는 동안 다음 공항으로 이동
            next_airport = graph[airport].pop()
            dfs(next_airport)
        route.append(airport)
        print("결과")

    dfs("ICN")
    return route[::-1]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# while True:
#     if airport not in graph:
#         break
#     if not graph[airport]:
#         break

######################################################
# 알파벳 순서가 앞서는 경로 : a > b
# pop 문법을 사용하므로 sort 시, reverse를 적용해야 한다.
